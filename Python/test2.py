import serial
import time

arduino = serial.Serial(port = 'COM19',baudrate = 115200, timeout=0)
time.sleep(2)

while True:

    print ("Enter '1' to turn 'on' the LED and '0' to turn LED 'off'")

    var = str(input())
    print ("You Entered :", var)

    arduino.write(str.encode(var))
    time.sleep(1)

    