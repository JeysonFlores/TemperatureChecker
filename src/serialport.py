import serial
import threading
import time

ser = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)
read = True
datos = ""


while True:
    if ser.in_waiting > 0:
        reading = ser.read(ser.in_waiting).decode('ascii')
        print(reading)
    ser.flush()