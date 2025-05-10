/*
 * View model for OctoPrint-Riskyupnpforward
 *
 * Author: Seth Foxen
 * License: AGPLv3
 */
function RiskyUPnPForwardViewModel(parameters) {
	console.log("RiskyUPnPForwardViewModel loaded");
    var self = this;
    self.settingsViewModel = parameters[0];

	//  I tried, but for the life of me I couldn't get the test button working. 
	//  I have no experience in JavaScript ┐(´ー｀)┌
	//  This whole file probably isn't needed, but I kept it in just in case
	//  I ever come back and figure this out.
    // self.testForward = function () {
		// console.log("testForward called");
        // const internal = self.settingsViewModel.settings.plugins.riskyupnpforward.internal_port();
        // const external = self.settingsViewModel.settings.plugins.riskyupnpforward.external_port();

        // $.ajax({
            // url: API_BASEURL + "plugin/riskyupnpforward",
            // type: "POST",
            // contentType: "application/json",
            // data: JSON.stringify({
                // command: "test_forward",
                // internal_port: internal,
                // external_port: external
            // }),
            // success: function (response) {
                // new PNotify({
                    // title: "Port Forwarding",
                    // text: response.message,
                    // type: "success"
                // });
            // },
            // error: function (xhr, status, error) {
                // new PNotify({
                    // title: "Error",
                    // text: "Failed to test port forwarding: " + xhr.responseText,
                    // type: "error"
                // });
            // }
        // });
    // };
}

OCTOPRINT_VIEWMODELS.push({
    construct: RiskyUPnPForwardViewModel,
    dependencies: ["settingsViewModel"],
    elements: ["#settings_plugin_riskyupnpforward"]
});
