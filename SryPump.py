
"""
Harvard Apparatus Pump 33 DDS Control Program
Author: Judicael Tombo

Description:
This Python program interfaces with the Harvard Apparatus Pump using pySerial.
It allows users to configure and control the pump via a command-line interface.
Designed to be modular and beginner-friendly.

Resources:
- Harvard Apparatus Pump Manual (Pump 33 DDS REV1):
  https://www.harvardapparatus.com/media/manuals/Product%20Manuals/Pump-33-DDS-Manual-5419-013-REV1.pdf
- pySerial Documentation:
  https://pyserial.readthedocs.io/en/latest/pyserial.html

Dependencies:
- pySerial (Install with `pip install pyserial`)
"""

import serial

# ============================ Serial Initialization ============================

def initialize_serial(port="COM4"):
    """Sets up the serial connection with the pump."""
    ser = serial.Serial(port=port)
    ser.baudrate = 9600                  # Data rate in bits per second
    ser.parity = serial.PARITY_NONE     # No parity bit
    ser.bytesize = 8                    # Number of data bits
    ser.stopbits = serial.STOPBITS_ONE  # Number of stop bits
    ser.xonxoff = False                 # Software flow control (off)
    ser.timeout = 5                     # Read timeout in seconds
    print(f"Serial connection initialized on {port}")
    return ser

# ============================ User Interaction ============================

def display_start_menu():
    """Displays the start menu and gets user input."""
    print("""
Welcome to the Harvard Apparatus Pump 33 DDS Program
----------------------------------------------------
1. Start Program
2. Quit Program
""")
    return input("Select an option: ")

def select_condition(ser):
    """Prompts user to select the pump condition mode."""
    conditions = {"1": "Independent", "2": "Reciprocating", "3": "Twin"}
    print("\nSelect a Condition Mode:")
    for key, value in conditions.items():
        print(f"{key}. {value}")
    choice = input("Selection: ")
    if choice in conditions:
        # Sending pump command according to manual: "condition MODE/"
        ser.write(f"condition {conditions[choice]}/\r".encode())
        print(f"{conditions[choice]} mode selected.")
        return choice
    else:
        print("Invalid selection. Please try again.")
        return select_condition(ser)

# ============================ Pump Class ============================

class Pump:
    """Represents the syringe pump and its operations."""
    def __init__(self, ser, mode):
        self.ser = ser
        self.mode = mode  # 1: Independent, 2: Reciprocating, 3: Twin

    def get_syringe_volume(self):
        """Fetches the current syringe volume setting from the pump."""
        command = b"svolume ab\r" if self.mode == "1" else b"svolume\r"
        # Command to retrieve volume setting; refer to manual under 'svolume'
        self.ser.write(command)
        response = self.ser.read(100)
        print("Syringe Volume:", response.decode())

    def set_syringe_volume(self):
        """Sets the syringe volume via user input."""
        if self.mode == "1":
            for pump in ['a', 'b']:
                vol = input(f"Enter volume for Pump {pump.upper()} (ul): ")
                # Command format: svolume a|b VALUE ul/
                self.ser.write(f"svolume {pump} {vol} ul/\r".encode())
        else:
            vol = input("Enter volume for both pumps (ul): ")
            self.ser.write(f"svolume {vol} ul/\r".encode())
        print("Syringe volume set successfully.")

# ============================ Main Program ============================

def main():
    # Step 1: Initialize serial connection
    ser = initialize_serial()

    # Step 2: Display start menu
    choice = display_start_menu()
    if choice != "1":
        print("Exiting program.")
        return

    # Step 3: Select condition (mode of operation)
    mode = select_condition(ser)

    # Step 4: Create a Pump object for further operations
    pump = Pump(ser, mode)

    # Step 5: Perform example actions
    pump.get_syringe_volume()
    pump.set_syringe_volume()

    print("Program complete. Extend this with more commands as needed.")

if __name__ == "__main__":
    main()
