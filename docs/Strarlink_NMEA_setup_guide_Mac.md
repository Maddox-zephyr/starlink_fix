Here is a step by step guide for the setup



Make sure you have **python** installed or find and install it. A quick google search should help.



# **Allow local location access in Starlink.**

 	You can enable location access by clicking the two bars at the top left corner in the app, then the info mark on the bottom right. You should be 	able to find the Debug data section and enable it from there. You can check if it works by typing 192.168.100.1 into the url bar in any browser. 	It should display the Debug data and amongst it the Location.

 	There is a full guide to do the enable location sharing on your Starlink here:

 	[https://maddox-zephyr.github.io/starlink\_position/starlink\_setup.html](https://maddox-zephyr.github.io/starlink_position/starlink_setup.html)






## Install the script
Download the **Starlink\_Data\_to\_NMEA\_mac.Zip** folder to any place you want and unzip it.

 	dont move files around, the Programm is expecting files to be in certain places. 





Open the **Starlink\_Data\_to\_NMEA** folder

&nbsp;	Open the **starlink-grpc-tools-main** folder

&nbsp;		find the **requirements.txt** file

&nbsp;		open **terminal** (it is pre installed on your mac)

&nbsp;			type 
``` python3 -m pip install -r ``` 
(drag and drop your requirements.txt file behind the r) and press enter

&nbsp;			It should now install all requirements.





Open the **Starlink\_Data\_to\_NMEA** folder 

 	open the **Starlink\_Data\_to\_NMEA\_V-1\_4\_MacOS.py** file in **IDLE**.

 	click on the window with the Code and press **run** (you should find that all the way at the Top of your screen).

&nbsp;	It should now transmit your Position.



For the setup it is important that your pc and nav device are in the same Starlink network.

 

 	Setup **OPENCPN**



 		Go to settings>Connect>Add New Connection

 

 		select Network

 		Network Protocol: UDP

 		Data Protocol: NMEA 0183

&nbsp;		Ip Address: 0.0.0.0

&nbsp;		DataPort: 30330

&nbsp;		Save changes



&nbsp;	Setup **Navionics**:

&nbsp;		0. Open Navionics

&nbsp;		1. Tap Menu

&nbsp;		2. Select Paired Devices

&nbsp;		2.5 Press + in the top right corner if available

&nbsp;		3. Add device manually

&nbsp;		4. Select UDP at the Bottom

&nbsp;		5. host: 0.0.0.0

&nbsp;		6. Port Number: 30330

&nbsp;		7. save

 



OpenCPN and navionics should now get the Starlink Locations and place your boat there.



This script sets the SOG to 0 if SOG is below 0.3 knots. this is to ensure that you dont Always have a speed and heading displayed while at anchor due to an inacurate position. you can change this in the Code.

