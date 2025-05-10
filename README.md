# Risky UPnP Forward



**Automatically forward a port to your OctoPrint instance using UPnP.**

>  **WARNING**: This plugin exposes your OctoPrint instance to the public internet. Only use this if you understand the security implications and have properly secured your OctoPrint setup (e.g., strong password, HTTPS, or VPN access).

>  By using this plugin, you acknowledge that **you are exposing a potentially sensitive device to the public internet**. It is your responsibility to secure your network and devices.

There are much safer ways to remotely access your OctoPrint server, and I wrote this plugin for personal use, but figured some other users might like to live dangerously as well. 
That's why it's called "Risky."

Check out NGROK(https://github.com/fieldOfView/OctoPrint-ngrok), Obico(https://github.com/TheSpaghettiDetective/OctoPrint-Obico), or OctoEverywhere(https://github.com/QuinnDamerell/OctoPrint-OctoEverywhere) for the PROPER tools for remote access.

---

## What It Does

Risky UPnP Forward attempts to automatically configure your router's port forwarding settings via UPnP. This allows external access to your OctoPrint server without manually changing router settings.

You can use it to forward a custom external port to your OctoPrint instance, and configure it to enable forwarding at startup and remove it on shutdown.

It'll also check for 'stale' forwarding rules, such as rules on your configured port that point to a different IP address, remove them, and update them. 
This is useful for devices that use DHCP for IP allocation.

---

## Features

- UPnP-based port mapping using `miniupnpc`
- Internal and external port configuration
- Toggle forwarding on OctoPrint startup/shutdown
- Safe defaults with user warnings(i.e NOT enabled by default ;P)

---

## Requirements

- OctoPrint >= 1.5.0  
- Python >= 3.7  
- `miniupnpc` Python package (installed automatically)

Your router must support and have UPnP enabled.

---

## Installation

You can install this plugin via the **Plugin Manager** by providing the URL to this repository:

https://github.com/sethfoxen/OctoPrint-RiskyUPnPForward


---

## Configuration

After installing, go to:

**Settings → Plugins → Risky UPnP Forward**

There you can:
- Set your **internal** OctoPrint port (usually 80 or 5000)
- Choose a public **external** port (e.g., 8080)
- Enable automatic forwarding on startup
- Remove the rule on shutdown

You'll have to restart OctoPrint for the changes to take affect. 
Be advised, some routers won't let you forward internal port 80, even if the external port is different.