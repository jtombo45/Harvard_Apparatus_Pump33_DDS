"""
============================================================
Harvard Apparatus Pump 33 DDS - Basic Control Script
============================================================

Description:
-------------
This Python script uses the `pySerial` library to interface 
with the Harvard Apparatus Pump via a serial connection. 

It demonstrates how to:
1. Configure syringe parameters (volume, diameter, target volume).
2. Set infusion rates.
3. Start the pump using INFUSE mode.

⚡ Note: This script is specifically designed for **infuse operations**.

Resources:
-----------
- Harvard Pump Manual (Pump 33 DDS REV1):
  https://www.harvardapparatus.com/media/manuals/Product%20Manuals/Pump-33-DDS-Manual-5419-013-REV1.pdf
- pySerial Documentation:
  https://pyserial.readthedocs.io/en/latest/pyserial.html

Terminology:
-------------
- **Infuse Mode**: Pump pushes fluid forward at a set rate.
- **Syringe Volume**: The total capacity of the syringe (µL).
- **Diameter**: Inner diameter of the syringe (mm) for accurate flow.
- **Target Volume**: The total volume to be infused before stopping.
- **Infusion Rate**: Speed at which fluid is dispensed (µL/min).

Ensure your pump is connected to the correct COM port before running.
"""

import serial

# ======================= Serial Configuration =======================

# Establish connection to the pump via COM4 (adjust if needed)
ser = serial.Serial(
    port="COM4",
    baudrate=9600,
    bytesize=8,
    timeout=5,
    stopbits=serial.STOPBITS_ONE,
    xonxoff=False,
    parity=serial.PARITY_NONE
)

print("Serial Connection Info:", ser)
print("Is Connection Open?:", ser.isOpen())

# ======================= Pump Configuration Commands =======================

# Each command follows the Harvard Apparatus syntax.
# Prefix '0' refers to Pump 0 (default pump index in multi-pump setups).

# 1️⃣ Set Syringe Volume (in µL)
command_string = b"0svolume 10 u/\r"
print("Setting Syringe Volume:", command_string)
ser.write(command_string)
response = ser.read(100)
print("Response:", response.decode())

# 2️⃣ Set Syringe Diameter (in mm)
command_string = b"0diameter 4\r"
print("Setting Syringe Diameter:", command_string)
ser.write(command_string)
response = ser.read(100)
print("Response:", response.decode())

# 3️⃣ Set Target Volume (total volume to infuse in µL)
command_string = b"0tvolume 4000 u\r"
print("Setting Target Volume:", command_string)
ser.write(command_string)
response = ser.read(100)
print("Response:", response.decode())

# 4️⃣ Set Infusion Rate (µL/min)
command_string = b"0irate 15 u/m\r"
print("Setting Infusion Rate:", command_string)
ser.write(command_string)
response = ser.read(100)
print("Response:", response.decode())

# 5️⃣ Start Infusion (Run Pump 0 in Infuse Mode)
command_string = b"0irun\r"
print("Starting Pump (Infuse Mode):", command_string)
ser.write(command_string)
response = ser.read(100)
print("Response:", response.decode())

# ======================= End of Script =======================
print("Pump configuration complete. Infusion started.")
