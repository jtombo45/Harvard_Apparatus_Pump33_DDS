#Description: 
################################################
# A program that uses pyserial to
# interface with the computer and the 
# Harvard apparatus pump. This program
# utilizes the infuse mode to control
# the pump. FYI this program is only
# meant for the infuse rate.

#Importing Pyserial (documentation: https://pyserial.readthedocs.io/en/latest/pyserial.html)
import serial 


def serInitializer(ser):
    ser.timout = 60 #timeout
    ser.baudrate = 9600 #baudrate
    ser.parity = serial.PARITY_NONE #parity 
    ser.bytesize = 8 #databits
    ser.stopbits = serial.STOPBITS_ONE #stopbits
    ser.xonxoff = False #Disable hardware (RTS/CTS) flow control. (Request To Send Ofkif)

def startPrompt(ser,userInput1):
    print("\nWelcome to the Harvard Apparutus Pump 33 DDS program")
    print("----------------------------------------------------")
    print("1. start program (1)")
    print("2. quit program (2)")
    userInput = input("Selection: ")

    if userInput == "1":
        userInput = condtPrompt(ser,userInput1)
    elif userInput == "2":
        print("Program ends")
    else:
        startPrompt(ser,userInput)

    return userInput
    

#Prompting user for the Condition Select
def condtPrompt(ser,userInput):
    print("Select a Condition:\n")
    print("\tIndependent (1)\n")
    print("\tReciprocating (2)\n")
    print("\tTwin (3)")
    userInput = input("Selection: ")

    if userInput == "1":
        #Command for independent condition
        command_string = b"condition Independent/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "2":
        #Command for reciprocating condition
        command_string = b"condition Reciprocating/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "3":
        #Command for twin condition
        command_string = b"condition Twin/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
    elif userInput == "4":
        print("Program ends")
    else:
        condtPrompt(ser,userInput)

    return userInput



##################################################
def syrConfigPrompt(ser,userInput):

    #Configuring the P1's volume/capacity (ul)
    userInput = input("Select P1's and P2's volume/capacity (ul): ")
    command_string = b"svolume " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)

    #Configuring P1's volume (mm)
    userInput = input("Select P1's and P2's diameter (mm): ")
    command_string = b"diameter " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)

    print("\nSelection Mode: \n")
    print("\t1. Run (1)\n")
    print("\t1. Quit (2)\n")
    userInput = input("Selection: ")

    if userInput == "1":
        #Configuring P1's and P2's infuse rate (ul/min)
        userInput = input("Select P1's and P2's infuse rate (ul/min): ")
        command_string = b"irate " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

        #Configuring P1's and P2's infuse rate (ul/min)
        userInput = input("Select P1's and P2's withdraw rate (ul/min): ")
        command_string = b"wrate " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

        #Configuring P1's and P2's target volume (ul)
        userInput = input("Select P1's and P2's target volume (ul): ")
        command_string = b"tvolume " + userInput.encode() + b" ul/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

    elif userInput == 2:
        print("Program ends")
    
    else:
        syrConfigPrompt1(ser,userInput)
        
    
    return userInput

def syrConfigPrompt1(ser,userInput):

    #Configuring the P1's volume/capacity (ul)
    userInput = input("Select P1's volume/capacity (ul): ")
    command_string = b"svolume a " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)
     #Configuring the P2's volume/capacity (ul)
    userInput = input("Select P2's volume/capacity (ul): ")
    command_string = b"svolume b " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)


    #Configuring P1's volume (mm)
    userInput = input("Select P1's diameter (mm): ")
    command_string = b"diameter a " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)
    #Configuring P2's volume (mm)
    userInput = input("Select P2's diameter (mm): ")
    command_string = b"diameter b " + userInput.encode() + b" ul/\r"
    #Sending/Writing the command to the pump
    ser.write(command_string)

    print("\nSelection Mode: \n")
    print("\t1. Run (1)\n")
    print("\t1. Quit (2)\n")
    userInput = input("Selection: ")

    if userInput == "1":
        #Configuring P1's infuse rate (ul/min)
        userInput = input("Select P1's infuse rate (ul/min): ")
        command_string = b"irate a " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
        #Configuring P2's infuse rate (ul/min)
        userInput = input("Select P2's infuse rate (ul/min): ")
        command_string = b"irate b " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

        #Configuring P1's infuse rate (ul/min)
        userInput = input("Select P1's withdraw rate (ul/min): ")
        command_string = b"wrate a " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
        #Configuring P1's infuse rate (ul/min)
        userInput = input("Select P2's withdraw rate (ul/min): ")
        command_string = b"wrate b " + userInput.encode() + b" u/m\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

        #Configuring the syring pump's target volume (ul)
        userInput = input("Select P1's target volume (ul): ")
        command_string = b"tvolume a " + userInput.encode() + b" ul/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)
        #Configuring the syring pump's target volume (ul)
        userInput = input("Select P2's target volume (ul): ")
        command_string = b"tvolume b " + userInput.encode() + b" ul/\r"
        #Sending/Writing the command to the pump
        ser.write(command_string)

    elif userInput == 2:
        print("Program ends")
    
    else:
        syrConfigPrompt1(ser,userInput)
        
    
    return userInput

def run(ser,userInput):
    #For independent mode:
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
                #Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "2":
                command_string = b"irun b\r"
                #Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "3":
                command_string = b"irun ab\r"
                #Sending/Writing the command to the pump
                ser.write(command_string)
            else:
                run(ser,userInput)

        elif userInput == "2":
            print("\nWhich pump to run?: \n")
            print("\t1.P1\n")
            print("\t2.P2\n")
            print("\t3.P1 and P2\n")
            userInput = input("Selection: ")
            if userInput == "1":
                command_string = b"wrun a\r"
                #Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "2":
                command_string = b"wrun b\r"
                #Sending/Writing the command to the pump
                ser.write(command_string)
            elif userInput == "3":
                command_string = b"wrun ab\r"
                #Sending/Writing the command to the pump
                ser.write(command_string)
            else:
                run(ser,userInput)
        else:
            run(ser,userInput)

    #For Twin and reciprocating
    elif userInput == "2":
        print("\nSelect Run Command: \n")
        print("\t1.Infuse\n")
        print("\t2.Withdrawl\n")
        userInput = input("Selection: ")

        if userInput == "1":
            command_string = b"irun\r"
            #Sending/Writing the command to the pump
            ser.write(command_string)
        
        elif userInput == "2":
            command_string = b"wrun\r"
            #Sending/Writing the command to the pump
            ser.write(command_string)
        else:
            run(ser,userInput)

    return userInput
    

########################################################################################################################################

def main():
    #Initializing pump through the serial port:
    ser = serial.Serial(port="COM4") #open serial port && #pen pump data stream:
    serInitializer(ser) #initializing properties of the ser object   
    #print(ser) #Prints out the ser objects properties
    #print(ser.isOpen()) #Prints True/False to see if the port is connected

    #Used to get user's input
    userInput  = None

    #Prompts the user if they want to start or end the program & its all used to initialize the pumpts condition
    userInput = startPrompt(ser,userInput)

    #Checking if the user wants to cont the program by checking the condition they selected
    if userInput == "1" or userInput == "2" or userInput == "3":
        if userInput == "1":
            #Configuring the P1's features
            userInput = syrConfigPrompt1(ser,userInput)
            userInput == "1"
            userInput = run(ser,userInput)
        elif userInput == "2" or userInput == "3":
            #Configuring the P1's features
            userInput = syrConfigPrompt(ser,userInput)
            userInput = "2"
            userInput = run(ser,userInput)


    else:
        #Prompts the user if they want to start or end the program & its all used to initialize the pumpts condition
        userInput = startPrompt(ser,userInput)



    
if __name__ == "__main__":
    main()