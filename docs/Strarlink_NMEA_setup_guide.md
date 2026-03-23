Here is a step by step guide for the setup



Make sure you have python installed or find and install it from the Microsoft store.


Allow local location access in Starlink.

&nbsp;	You can enable location access by clicking the two bars at the top left corner in the app, then the info mark on the bottom right. You should be 	able to find the Debug data section and enable it from there. You can check if it works by typing 192.168.100.1 into the url bar in any browser. 	It should display the Debug data and amongst it the Location.

&nbsp;	There is a full guide to do the enable location sharing on your Starlink here:

&nbsp;	[https://maddox-zephyr.github.io/starlink\_position/starlink\_setup.html](https://maddox-zephyr.github.io/starlink_position/starlink_setup.html)







Download the Starlink\_Data\_to\_NMEA.Zip folder to any place you want and unzip it.

 	dont move files around, the Programm is expecting files to be in certain places. 





Open the Starlink\_Data\_to\_NMEA folder

 	Run the Run\_Starlink\_Bridge\_windows.bat file on Windows.

 	It should install the requirements and once it is done start broadcasting positions.



 	For the setup it is important that your pc and nav device are in the same Starlink network.

 	Setup OPENCPN



 		Go to settings>Connect>Add New Connection

 

 		select Network

 		Network Protocol: UDP

 		Data Protocol: NMEA 0183

 		Ip Address: 0.0.0.0

 		DataPort: 30330

 		Save changes



 	Setup Navionics:

 		0. Open Navionics

 		1. Tap Menu

 		2. Select Paired Devices

 		2.5 Press + in the top right corner if available

 		3. Add device manually

 		4. Select UDP at the Bottom

 		5. host: 0.0.0.0

 		6. Port Number: 30330

 		7. save

 



OpenCPN and navionics should now get the Starlink Locations and place your boat there.



This script sets the SOG to 0 if SOG is below 0.3 knots. this is to ensure that you dont Always have a speed and heading displayed while at anchor due to an inacurate position. you can change this in the Code.

