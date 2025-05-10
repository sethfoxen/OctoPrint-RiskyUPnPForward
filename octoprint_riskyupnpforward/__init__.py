import octoprint.plugin
import miniupnpc
import flask

#  Hello world! :3

class RiskyUPnPForwardPlugin(octoprint.plugin.StartupPlugin,
                              octoprint.plugin.ShutdownPlugin,
                              octoprint.plugin.SettingsPlugin,
                              octoprint.plugin.TemplatePlugin):

    def on_after_startup(self):
        if not self._settings.get_boolean(["enable_on_startup"]):
            self._logger.info("UPnP port forwarding disabled on startup.")
            return

        internal_port = self._settings.get_int(["internal_port"])
        external_port = self._settings.get_int(["external_port"])
        self._logger.info(f"Attempting to forward {external_port} → {internal_port}")

        try:
            self.upnp = miniupnpc.UPnP()
            self.upnp.discoverdelay = 200
            self.upnp.discover()
            self.upnp.selectigd()

            local_ip = self.upnp.lanaddr
            existing_mapping = self.upnp.getspecificportmapping(external_port, 'TCP')

            #  Check for stale port mapping
            if existing_mapping:
                mapped_ip, _, _, _, _ = existing_mapping
                if mapped_ip != local_ip:
                    self._logger.warning(
                        f"UPnP mapping exists but points to {mapped_ip} instead of this device ({local_ip}). "
                        "Your network may have reassigned your IP (e.g., switching Wi-Fi to Ethernet, or DHCP lease expiring)."
                    )
                    #  Remove the stale mapping
                    self.upnp.deleteportmapping(external_port, 'TCP')
                    self._logger.info("Removed stale mapping; re-adding with current IP.")

            self.upnp.addportmapping(external_port, 'TCP', local_ip, internal_port, 'OctoPrint UPnP', '')
            self._logger.info(f"Port successfully forwarded: {external_port} → {local_ip}:{internal_port}")

        except Exception as e:
            self._logger.error(f"Failed to configure port mapping: {e}")
            self.upnp = None

    ## SettingsPlugin mixin
    def get_settings_defaults(self):
        return dict(
            internal_port=5000,
            external_port=5000,
            enable_on_startup=False,
            remove_on_shutdown=True
        )

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]


    def on_shutdown(self):
        if not self._settings.get_boolean(["remove_on_shutdown"]):
            return

        if hasattr(self, 'upnp') and self.upnp:
            external_port = self._settings.get_int(["external_port"])
            try:
                self.upnp.deleteportmapping(external_port, 'TCP')
                self._logger.info(f"Removed port mapping on shutdown: {external_port}")
            except Exception as e:
                self._logger.error(f"Failed to remove port mapping: {e}")

    def get_api_commands(self):
        return dict(test_forward=[])

    ##  I couldn't get the test button to work and it would endlessly hang the settings page,
    ##  so I just commented it out; This function is unused. "( – o – )=3
    # def on_api_command(self, command, data):
        # if command == "test_forward":
            # try:
                # internal_port = self._settings.get_int(["internal_port"])
                # external_port = self._settings.get_int(["external_port"])

                # upnp = miniupnpc.UPnP()
                # upnp.discoverdelay = 200
                # upnp.discover()
                # upnp.selectigd()
                # local_ip = upnp.lanaddr

                # existing_mapping = upnp.getspecificportmapping(external_port, 'TCP')
                # if existing_mapping:
                    # mapped_ip, _, _, _, _ = existing_mapping
                    # if mapped_ip != local_ip:
                        # upnp.deleteportmapping(external_port, 'TCP')

                # upnp.addportmapping(external_port, 'TCP', local_ip, internal_port, 'OctoPrint UPnP Test', '')
                # return flask.jsonify(message=f"Port {external_port} forwarded to {local_ip}:{internal_port}")
            # except Exception as e:
                # self._logger.exception("Manual port forwarding failed")
                # flask.abort(500, description=f"UPnP error: {e}")

    def get_assets(self):
        return {
            "js": ["js/RiskyUPnPForward.js"]
        }

__plugin_name__ = "Risky UPnP Forward"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_implementation__ = RiskyUPnPForwardPlugin()
__plugin_js__ = ["static/js/RiskyUPnPForward.js"]
