import serial

zaber = serial.Serial('COM3', 115200, timeout=1)  # Set an appropriate timeout value in seconds

# Send a command to the Zaber motor
command ="/1 move rel 10000\n"  # Replace this with the actual command you want to send
zaber.write(command.encode())

# Read the response from the Zaber motor
response = zaber.read(100)  # Replace 100 with an appropriate buffer size

if response:
    print("Received:", response)
else:
    print("No response within the timeout period.")

zaber.close()  # Close the serial port when done
