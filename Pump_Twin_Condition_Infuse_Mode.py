#Description: 
################################################
# A program that uses pyserial to
# interface with the computer and the 
# Harvard apparatus pump. This program
# utilizes the infuse mode to control
# the pump. FYI this program is only
# meant for the infuse rate.

#Terminology:
################################################



#Importing Pyserial (documentation: https://pyserial.readthedocs.io/en/latest/pyserial.html)
import serial 

#Configuring Serial to interface between computer and Harvard Appartus pump:
################################################
#Configuring serial object and connecting to the pump
ser = serial.Serial(port="COM4", baudrate=9600, bytesize=8, timeout=5, stopbits=serial.STOPBITS_ONE, xonxoff=False, parity=serial.PARITY_NONE)
#Printing the serial object
print(ser)
# Checking if the connection is truly open
print(ser.isOpen())

# Setting the Syringe Volume:
###############################################
#Setting up the syringe pump's volume in ul
command_string = b"0svolume 10 u/\r"
print(command_string)
#Sending/Writing the command to the pump
ser.write(command_string)
#Receiving the pump's response to command within a 10 seconds
response = ser.read(100)
#Printing out the pump's response
print(response.decode())

#Syringe Diameter:
################################################
#Setting up the syringe pump's diameter in mm
command_string = b"0diameter 4\r"
print(command_string)
#Sending/Writing the command to the pump
ser.write(command_string)
#Receiving the pump's response to command within a 10 seconds
response = ser.read(100)
#Printing out the pump's response
print(response.decode())

#Setting the Target Volume:
################################################
#Setting the pump zero target volume in ul
command_string = b"0tvolume 4000 u\r"
print(command_string)
#Sending/Writing the command to the pump
ser.write(command_string)
#Receiving the pump's response to command within a 10 seconds
response = ser.read(100)
#Printing out the pump's response
print(response.decode())


#Infusion Rate # ul/mm:
################################################
#Setting up the syringe pump zero infusion rate max in ul/min
command_string = b"0irat 15 u/m\r"
print(command_string)
#Sending/Writing the command to the pump
ser.write(command_string)
#Receiving the pump's response to command within a 10 seconds
response = ser.read(100)
#Printing out the pump's response
print(response.decode())

#Run Pump Zero:
################################################
#Setting the pump zero infusion rate max as 15 ul
command_string = b"0irun\r"
print(command_string)
#Sending/Writing the command to the pump
ser.write(command_string)
#Receiving the pump's response to command within a 10 seconds
response = ser.read(100)
#Printing out the pump's response
print(response.decode())
