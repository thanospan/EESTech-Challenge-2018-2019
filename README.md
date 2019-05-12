# EESTech Challenge 2018-2019
This project was implemented during the [EESTech Challenge](https://eestechchallenge.eestec.net/) Patras 2018-2019.</br>

- <b>Topic</b>: Internet of Things
- <b>Goal</b>: Build elements of a smart classroom utilizing low-cost IoT devices, well established open-source libraries and cloud technologies.
- <b>Tasks</b>:
	1. Setup and connect to an IoT device to monitor the environmental conditions of the classroom. Transmit the data collected from the sensors to the Cloud.
	2. Setup a secure, bi-directional communication between the IoT devices and the Cloud. Collect telemetry data from multiple IoT devices, store and analyze the data centrally. 


Team Members: [Thanos Panagiotidis](https://github.com/thanospan/), [Nikos Nikolaidis](https://github.com/nikon95), [Orestis Nikolas](https://github.com/OrestisDrow)

## Hardware/Software
* [DA14585 IoT Multi Sensor Add-On Board](https://www.dialog-semiconductor.com/products/da14585-iot-multi-sensor-development-kit/)

* Raspberry Pi 3 Model B
	- [Raspbian Stretch](https://www.raspberrypi.org/downloads/raspbian/)
	- Python 3.5.3
	- [bluepy](https://github.com/IanHarvey/bluepy/)
	- [paho-mqtt](https://pypi.org/project/paho-mqtt/)

* Cloud (DigitalOcean)
	- Ubuntu 18.04 VM
	- Docker
	- [nodered/node-red-docker](https://hub.docker.com/r/nodered/node-red-docker/)
	- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto/)
	- [mysql/mysql-server](https://hub.docker.com/r/mysql/mysql-server/)

## Architecture
<p align="center"><img src="https://i.imgur.com/RXuZimW.png"></p>

## Usage
* Turn on the DA14585 IoT Multi Sensor Add-On Board by moving the switch.</br>
(Move the device if it has been inactive for more than 60 seconds.)

* Cloud</br>
	- Create an Ubuntu 18.04 Virtual Machine and login as a user with root privileges.

	- Clone the project:
	```
	$ git clone https://github.com/thanospan/EESTech-Challenge-2018-2019.git
	$ cd EESTech-Challenge-2018-2019/Cloud
	```
	
	- Run the setup script:
	```
	$ bash setup
	```
	
	- Open a browser and visit <b>http://{vm-ip-address}:{node-red-port}</b> to access the Node-RED editor.
	
	- Double click on one of the MySQL nodes.</br>
	Click the button next to the select box to edit the MySQL database node.</br>
	Set the User, Password fields to the username and password of the MySQL user created to access Node-RED.
	
	- Open a browser and visit <b>http://{vm-ip-address}:{node-red-port/ui}</b> to access the Node-RED dashboard.
	
	---
	
	A Step-By-Step Guide on how to set up the Ubuntu 18.04 VM can be found [here](https://github.com/thanospan/EESTech-Challenge-2018-2019/wiki/Cloud-Setup).
	
	---

* Raspberry Pi
	- Install bluepy:
	```
	$ sudo apt install python3-pip libglib2.0-dev
	$ sudo pip3 install bluepy
	```
	
	- Install paho-mqtt:
	```
	$ sudo pip3 install paho-mqtt
	```
	
	- Clone the project:
	```
	$ git clone https://github.com/thanospan/EESTech-Challenge-2018-2019.git
	$ cd EESTech-Challenge-2018-2019/RPi
	```	
	
	- Change the variables in get_data.py and run:
	```
	$ python3 get_data.py
	```

## Disclaimer
It is highly advised that some additional security steps are taken.</br>
More information can be found here:</br>
- https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04</br>
- https://nodered.org/docs/security</br>
- https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-18-04</br>

<b>Use with caution!</b>


