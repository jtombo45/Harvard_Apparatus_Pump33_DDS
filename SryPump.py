# Description:
################################################
# A program that uses pyserial to
# interface with the computer and the
# Harvard apparatus pump. This program
# utilizes the infuse mode to control
# the pump. FYI this program is only
# meant for the infuse rate.
# Importing Pyserial (documentation:
# https://pyserial.readthedocs.io/en/latest/pyserial.html)
import serial
import math


def serInitializer(ser):

    ser.baudrate = 9600  # baudrate
    ser.parity = serial.PARITY_NONE  # parity
    ser.bytesize = 8  # databits
    ser.stopbits = serial.STOPBITS_ONE  # stopbits
    # Disable hardware (RTS/CTS) flow control. (Request To Send Ofkif)
    ser.xonxoff = False
    ser.timeout = 5  # timeout


def startPrompt(ser, userInput1):
    print("\nWelcome to the Harvard Apparutus Pump 33 DDS program")
    print("----------------------------------------------------")
    print("1. start program (1)")
    print("2. quit program (2)")
    userInput = input("Selection: ")

    if userInput == "1":
        userInput = condtPrompt(ser, userInput1)
    elif userInput == "2":
        print("Program ends")
    else:
        startPrompt(ser, userInput)

    return userInput


# Prompting user for the Condition Select
def condtPrompt(ser, userInput):
    print("Select a Condition:\n")
    print("\tIndependent (1)\n")
    print("\tReciprocating (2)\n")
    print("\tTwin (3)")
    userInput = input("Selection: ")

    if userInput == "1":
        # Command for independent condition
        command_string = b"condition Independent/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "2":
        # Command for reciprocating condition
        command_string = b"condition Reciprocating/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "3":
        # Command for twin condition
        command_string = b"condition Twin/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "4":
        print("Program ends")
    else:
        condtPrompt(ser, userInput)

    return userInput

# For twin or recripocal mode


def syrConfigPrompt(ser, userInput):

    # Configuring the P1's volume/capacity (ul)
    userInput = input("Select P1's and P2's volume/capacity (ul): ")
    command_string = b"svolume " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)

    # Configuring P1's volume (mm)
    userInput = input("Select P1's and P2's diameter (mm): ")
    command_string = b"diameter " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)

    print("\nSelection Mode: \n")
    print("\t1. Run (1)\n")
    print("\t1. Quit (2)\n")
    userInput = input("Selection: ")

    if userInput == "1":
        # Configuring P1's and P2's infuse rate (ul/min)
        userInput = input("Select P1's and P2's infuse rate (ul/min): ")
        command_string = b"irate " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

        # Configuring P1's and P2's infuse rate (ul/min)
        userInput = input("Select P1's and P2's withdraw rate (ul/min): ")
        command_string = b"wrate " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

        # Configuring P1's and P2's target volume (ul)
        userInput = input("Select P1's and P2's target volume (ul): ")
        command_string = b"tvolume " + userInput.encode() + b" ul/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

    elif userInput == 2:
        print("Program ends")

    else:
        syrConfigPrompt1(ser, userInput)

    return userInput

# For independent mode


def syrConfigPrompt1(ser, userInput):

    # Configuring the P1's volume/capacity (ul)
    userInput = input("Select P1's volume/capacity (ul): ")
    command_string = b"svolume a " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)
    # Configuring the P2's volume/capacity (ul)
    userInput = input("Select P2's volume/capacity (ul): ")
    command_string = b"svolume b " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)

    # Configuring P1's volume (mm)
    userInput = input("Select P1's diameter (mm): ")
    command_string = b"diameter a " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)
    # Configuring P2's volume (mm)
    userInput = input("Select P2's diameter (mm): ")
    command_string = b"diameter b " + userInput.encode() + b" ul/\r"
    # Sending/Writing the command to the pump
    ser.write(command_string)

    print("\nSelection Mode: \n")
    print("\t1. Run (1)\n")
    print("\t1. Quit (2)\n")
    userInput = input("Selection: ")

    if userInput == "1":
        # Configuring P1's infuse rate (ul/min)
        userInput = input("Select P1's infuse rate (ul/min): ")
        command_string = b"irate a " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
        # Configuring P2's infuse rate (ul/min)
        userInput = input("Select P2's infuse rate (ul/min): ")
        command_string = b"irate b " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

        # Configuring P1's infuse rate (ul/min)
        userInput = input("Select P1's withdraw rate (ul/min): ")
        command_string = b"wrate a " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
        # Configuring P1's infuse rate (ul/min)
        userInput = input("Select P2's withdraw rate (ul/min): ")
        command_string = b"wrate b " + userInput.encode() + b" u/m\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

        # Configuring the syring pump's target volume (ul)
        userInput = input("Select P1's target volume (ul): ")
        command_string = b"tvolume a " + userInput.encode() + b" ul/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)
        # Configuring the syring pump's target volume (ul)
        userInput = input("Select P2's target volume (ul): ")
        command_string = b"tvolume b " + userInput.encode() + b" ul/\r"
        # Sending/Writing the command to the pump
        ser.write(command_string)

    elif userInput == 2:
        print("Program ends")

    else:
        syrConfigPrompt1(ser, userInput)

    return userInput


def run(ser, userInput):
    # For independent mode:
    if userInput == "1":
        print("\nSelect Run Command: \n")
        print("\t1.Infuse\n")
        print("\t2.Withdrawl\n")
        userInput = input("Selection: ")

        if userInput == "1":
            print("\nWhich pump to run?: \n")
            print("\t1.P1\n")
            print("\t2.P2\n")
            print("\t3.P1 and P2\n")
            userInput = input("Selection: ")
            if userInput == "1":
                command_string = b"irun a\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "2":
                command_string = b"irun b\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "3":
                command_string = b"irun ab\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            else:
                run(ser, userInput)

        elif userInput == "2":
            print("\nWhich pump to run?: \n")
            print("\t1.P1\n")
            print("\t2.P2\n")
            print("\t3.P1 and P2\n")
            userInput = input("Selection: ")
            if userInput == "1":
                command_string = b"wrun a\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "2":
                command_string = b"wrun b\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "3":
                command_string = b"wrun ab\r"
                # Sending/Writing the command to the pump
                ser.write(command_string)
            else:
                run(ser, userInput)
        else:
            run(ser, userInput)

    # For Twin and reciprocating
    elif userInput == "2":
        print("\nSelect Run Command: \n")
        print("\t1.Infuse\n")
        print("\t2.Withdrawl\n")
        userInput = input("Selection: ")

        if userInput == "1":
            command_string = b"irun\r"
            # Sending/Writing the command to the pump
            ser.write(command_string)

        elif userInput == "2":
            command_string = b"wrun\r"
            # Sending/Writing the command to the pump
            ser.write(command_string)
        else:
            run(ser, userInput)

        print("Command:\n")
        print("\t1.Stop")
        print("\t2.Continue")
        userInput = input("Selection: ")

    return userInput


def userPrompt():
    print("Select Commands:")
    print("-------------------------------\n")
    print("Getter Methods:\n")
    print("\t1. Get Syringe Volume")
    print("\t2. Get Syringe Diameter")
    print("\t3. Get Infuse rate ul/min")
    print("\t4. Get Withdraw rate ul/min")
    print("\t5. Get Target Volume ul\n")
    print("Setter Methods:\n")
    print("\t6. Set Syringe Volume")
    print("\t7. Set Syringe Diameter")
    print("\t8. Set Infuse rate ul/min")
    print("\t9. Set Withdraw rate ul/min")
    print("\t10. Set Target Volume ul")
    print("\t11. Run Withdrawl\\Infuse")
    print("\t12. Stop pump")
    print("\t13. End Program")


class Pump:
    def __init__(self, ser, mode):
        self.ser = ser
        # Used to track the mode of the syring pump: independent (1),
        # Recripocal (2), and Twin or Recripocal Mode
        self.mode = mode

    def getSyrPumpVol(self, ser, mode):
        print("\nMethod: getSyrPumpVol\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if self.mode == "1":
            command_string = b"svolume ab\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            # Printing out the pump's response
            print(response.decode())
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            command_string = b"svolume\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            # Printing out the pump's response
            print(response.decode() + "\n")

    def setSyrPumpVol(self, ser, mode):
        print("\nMethod: setSyrPumpVol\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
            # Configuring the P1's volume/capacity (ul)
            userInput = input("Select P1's volume/capacity (ul): ")
            command_string = b"svolume a " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Configuring the P2's volume/capacity (ul)
            userInput = input("Select P2's volume/capacity (ul): ")
            command_string = b"svolume b " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring the P1 and P2's volume/capacity (ul)
            userInput = input("Select P1's and P2's volume/capacity (ul): ")
            command_string = b"svolume " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def getSyrDiameter(self, ser, mode):
        print("\nMethod: getSyrDiameter\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
            command_string = b"diameter\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            # Printing out the pump's response
            print(response.decode())
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            command_string = b"diameter ab\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            # Printing out the pump's response
            print(response.decode() + "\n")

    def setSyrDiameter(self, ser, mode):
        print("\nMethod: setSyrDiameter\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
           # Configuring P1's volume (mm)
            userInput = input("Select P1's diameter (mm): ")
            command_string = b"diameter a " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Configuring P2's volume (mm)
            userInput = input("Select P2's diameter (mm): ")
            command_string = b"diameter b " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring P1's volume (mm)
            userInput = input("Select P1's and P2's diameter (mm): ")
            command_string = b"diameter " + userInput.encode() + b" ul/\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def getTargetVol(self, ser, mode):
        print("\nMethod: getTargetVol\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
            command_string = b"tvolume ab\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            command_string = b"tvolume\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())

    def setTargetVol(self, ser, mode):
        print("\nMethod: getSyrDiameter\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
           # Configuring P1's infuse rate (ul/min)
            userInput = input("Select P1's target volume (ul): ")
            command_string = b"tvolume a " + userInput.encode() + b" u\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Configuring P2's infuse rate (ul/min)
            userInput = input("Select P2's target volume (ul): ")
            command_string = b"tvolume b " + userInput.encode() + b" u\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring P1's and P2's infuse rate (ul/min)
            userInput = input("Select P1's and P2's infuse rate (ul/min): ")
            command_string = b"tvolume " + userInput.encode() + b" u\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def getInfRate(self, ser, mode):
        # Independent mode:
        if mode == "1":
            command_string = b"irate ab\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            command_string = b"irate\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())

    def setInfRate(self, ser, mode):
        print("\nMethod: setInfRate\n ser timeout = " + str(self.ser.timeout))
        # Independent mode:
        if mode == "1":
           # Configuring P1's infuse rate (ul/min)
            userInput = input("Select P1's infuse rate (ul/min): ")
            command_string = b"irate a " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Configuring P2's infuse rate (ul/min)
            userInput = input("Select P2's infuse rate (ul/min): ")
            command_string = b"irate b " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring P1's and P2's infuse rate (ul/min)
            userInput = input("Select P1's and P2's infuse rate (ul/min): ")
            command_string = b"irate " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def getWRate(self, ser, mode):
        # Independent mode:
        if mode == "1":
            command_string = b"wrate ab\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            command_string = b"wrate\r"
            print(command_string)
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Receiving the pump's response to command within a 100 bytes
            response = self.ser.read(100)
            print(response.decode())

    def setWRate(self, ser, mode):
        # Independent mode:
        if mode == "1":
           # Configuring P1's withdrawl rate (ul/min)
            userInput = input("Select P1's withdrawl rate (ul/min): ")
            command_string = b"wrate a " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
            # Configuring P2's withdrawl rate (ul/min)
            userInput = input("Select P2's withdrawl rate (ul/min): ")
            command_string = b"wrate b " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring P1's and P2's infuse rate (ul/min)
            userInput = input("Select P1's and P2's withdrawl rate (ul/min): ")
            command_string = b"wrate " + userInput.encode() + b" u/m\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def stopPump(self, ser, mode):
        # Independent mode:
        if mode == "1":
            # Configuring P1's withdrawl rate (ul/min)
            print("Program is stopped")
            command_string = b"stop ab\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)
        # Twin or Recripocal mode:
        elif mode == "2" or mode == "3":
            # Configuring P1's withdrawl rate (ul/min)
            print("Pump is stopped")
            command_string = b"stop\r"
            # Sending/Writing the command to the pump
            self.ser.write(command_string)

    def run(self, ser, mode):
        # For independent mode:
        if mode == "1":
            print("\nSelect Run Command: \n")
            print("\t1.Infuse\n")
            print("\t2.Withdrawl\n")
            mode = input("Selection: ")

            if mode == "1":
                print("\nWhich pump to run?: \n")
                print("\t1.P1\n")
                print("\t2.P2\n")
                print("\t3.P1 and P2\n")
                mode = input("Selection: ")
                if mode == "1":
                    command_string = b"irun a\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                elif mode == "2":
                    command_string = b"irun b\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                elif mode == "3":
                    command_string = b"irun ab\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                else:
                    run(self.ser, mode)

            elif mode == "2":
                print("\nWhich pump to run?: \n")
                print("\t1.P1\n")
                print("\t2.P2\n")
                print("\t3.P1 and P2\n")
                mode = input("Selection: ")
                if mode == "1":
                    command_string = b"wrun a\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                elif mode == "2":
                    command_string = b"wrun b\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                elif mode == "3":
                    command_string = b"wrun ab\r"
                    # Sending/Writing the command to the pump
                    self.ser.write(command_string)
                else:
                    run(self.ser, mode)
            else:
                run(self.ser, mode)

        # For Twin and reciprocating
        elif mode == "2":
            print("\nSelect Run Command: \n")
            print("\t1.Infuse\n")
            print("\t2.Withdrawl\n")
            mode = input("Selection: ")

            if mode == "1":
                command_string = b"irun\r"
                # Sending/Writing the command to the pump
                self.ser.write(command_string)

            elif mode == "2":
                command_string = b"wrun\r"
                # Sending/Writing the command to the pump
                self.ser.write(command_string)
            else:
                run(self.ser, mode)

def main():
    # Initializing pump through the serial port:
    # open serial port && #pen pump data stream:
    ser = serial.Serial(port="COM4")
    serInitializer(ser)  # initializing properties of the ser object
    print("\nser timeout = " + str(ser.timeout) + "\n")
    # Prints out the ser objects properties
    print("Ser object information: " + str(ser) + "\n")
    # Prints True/False to see if the port is connected
    print("Is ser object open: " + str(ser.isOpen()) + "\n")

    # Used to get user's input
    userInput = None
    # Used to track the mode of the syring pump: independent (1), Recripocal
    # (2), and Twin or Recripocal Mode
    mode = 0

    # Prompts the user if they want to start or end the program & its all used
    # to initialize the pumpts condition
    userInput = startPrompt(ser, userInput)
    mode = userInput

    print("\nmode: " + str(mode) + "\n")
    # Checking if the user wants to cont the program by checking the condition
    # they selected
    if userInput == "1" or userInput == "2" or userInput == "3":
        # Used for independent mode
        if userInput == "1":
            # Configuring the P#'s features
            userInput = syrConfigPrompt1(ser, userInput)
            userInput = "1"
            userInput = run(ser, userInput)

        # Used for Twin or Recripocal Mode
        elif userInput == "2" or userInput == "3":
            # Configuring the P#'s features
            userInput = syrConfigPrompt(ser, userInput)
            userInput = "2"
            userInput = run(ser, userInput)
        # Creating instance of a pump object
        pump = Pump(ser, mode)
    # If user selects the wrong input we prompt them again
    else:
        # Prompts the user if they want to start or end the program & its all
        # used to initialize the pumpts condition
        userInput = startPrompt(ser, userInput)

    #Calculating Pressure
    

    # Prompting the user
    userPrompt()
    userInput = input("Selection: ")
    while userInput != "13":
        # Get Syringe Volume"
        if userInput == "1":
            pump.getSyrPumpVol(ser, mode)
        # Get Syringe Diameter
        elif userInput == "2":
            pump.getSyrDiameter
        # Get Infuse rate ul/min
        elif userInput == "3":
            pump.getInfRate(ser, mode)
        # Get Withdraw rate ul/min
        elif userInput == "4":
            pump.getWRate(ser, mode)
        # Get Target Volume ul
        elif userInput == "5":
            pump.getTargetVol(ser, mode)
        # Set Syring Volume ul
        elif userInput == "6":
            pump.setSyrPumpVol(ser, mode)
        # Set Syringe Diameter
        elif userInput == "7":
            pump.setSyrDiameter(ser, mode)
        # Set Infuse rate ul/min
        elif userInput == "8":
            pump.setInfRate(ser, mode)
        # Set Withdraw rate ul/min
        elif userInput == "9":
            pump.setWRate(ser, mode)
        # Set Target Volume ul
        elif userInput == "10":
            pump.setTargetVol(ser, mode)
        # Run Withdrawl\Infuse
        elif userInput == "11":
            run(ser, mode)
        # Stop pump
        elif userInput == "12":
            pump.stopPump(ser, mode)

        userPrompt()
        userInput = input("Selection: ")

    if userInput == "2":
        a = None
        # After the program


if __name__ == "__main__":
    main()
