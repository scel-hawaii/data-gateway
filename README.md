# data-gateway
Data gateway for a generic sensor network

# Production Procedure

Run the following command in the top level directory:

    ./run_production.sh

# Testing Procedure

To enjoy the packet_tester.py program, first download or clone the repository at https://github.com/scel-hawaii/data-gateway

Equipment Needed:
  Computer
  USB XBee Explorer
  Male to Male USB 2.0 to µUSB
  An XBee configured to your weatherbox's XBee

**Make sure you are in the data-gateway directory when attempting to run the program**
Instructions for running the gateway_server program on your personal computer:

	Step 1: Connect your Xbee device to the explorer, and plug that into your computer
	Step 2: Install python(refer to https://wiki.scel-hawaii.org/doku.php?id=training:python)
	Step 3: Update pip on your computer
		if Windows:
			run the following command: python -m pip install -U pip setuptools
		if Mac or Linux:
			run the following command: pip install -U pip setuptools
	Step 4: Install the following python packages using these commands (if issues run as administrator):
		pip install xbee
		pip install pyserial
	Step 5: Locate your serial port by using the following command:
		if Windows:
			in the command prompt use the command: mode
			look for the COM name of the serial port ex: 'COM3'
			insert the name when prompted by the program
		if Mac:
			in the command line use the command: ls /dev/cu.*
			locate the path of your serial port. ex: /dev/cu.usbserial-DN01DS4M
			insert the path when you are prompted by the program
		if Linux:
			in the command line use the command: dmseg
			locate FTDI USB serial device line and remember the port it is attached to. ex: ttyUSB0
			When you are prompted by the program insert the following string: /dev/"YOURPORTHERE"
										      ex: /dev/ttyUSB0
	Step 6: Run the program with the command: python gateway_server.py (make sure you're in the src folder)
