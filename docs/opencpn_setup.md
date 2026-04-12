# Starlink Python bridge for Windows
Versions of this script have, in 2026, guided 60+ boats safely through the Red Sea. Basically, all boats have experienced GPS outages on their journey, but could use Starlink to navigate safely. It has been designed to be easy to use by everyone, and as long as the bridge is running, it can send the Starlink position to all devices in the network. There is both a video and a written tutorial for the setup to make it as easy to use as possible. 

## Get the OpenCPN-Starlink zip file

- Send your browser to the [URL to download the Starlink_data_to_NMEA.zip file](https://github.com/Maddox-zephyr/starlink_position/releases)
- Under the most recent release, expand the Assets dropdown.
- Click on the Starlink_data_to_NMEA.zip file to
download the zip file to your computer
- Move the file to any place you want on your computer and unzip it into a folder.

## Video Setup
[This video tutorial is the easiest way to understand the setup process](https://youtu.be/vWmSpZMmEbg)

## Starlink->OpenCPN or Navionics setup

Using OpenCPN with Starlink involves setting up a bridge
that forwards Starlink's location data to OpenCPN.
Here is a step by step guide for configuring the Starlink->OpenCPN
bridge.

All the following steps must be done on the computer (Windows or Linux)
that you are going to run the OpenCPN-Starlink software on.

## Prerequisites

Make sure you have python installed (a quick google search should help)

Make sure you have enabled location access on the Starlink antenna by
following the steps on [this page](https://maddox-zephyr.github.io/starlink_position/starlink_setup.html)

## Start the Starlink data bridge software

- Open the unzipped Starlink_data_to_NMEA folder and find the 
```
Run_Starlink_Bridge_windows.bat
```
file. Double-click on the file. 

-The script should install the dependencies and then start transmitting data, looking something like this:
```
Sent: 35.1971, 25.7165 | SOG: 0.0kn, COG: 0°
```

# Setup OPENCPN

- In OpenCPN, go to settings>Connect>Add New Connection
- Configure the new connection as follows:		
    - select Network
    - Network Protocol: UDP
    - Data Protocol: NMEA 0183
    - Ip Address: 0.0.0.0
    - DataPort: 30330
- Save your changes

# Setup Navionics:

1. Tap Menu
2. Select Paired Devices
3. Add device manually
4. Select UDP at the Bottom
5. host: 0.0.0.0
6. Port Number: 30330

# Run the system

OpenCPN and navionics should now get the Starlink Locations and place
your boat there.
 
This script sets the SOG to 0 if SOG is below 0.3
knots. This is to ensure that you dont have a speed and heading
displayed while at anchor. You can change this in the code.
