import serial
from threading import Thread
from __main__ import Temperatures, db, cfg

ser = serial.Serial(cfg["app"]["arduino"]["port"], 9600, timeout=1)
read = True
datos = ""

def save_to_database(temp):
    try:
        new_temp = Temperatures(float(temp))
        db.session.add(new_temp)
        db.session.commit()
    except Exception as e:
        print('Error en la base de datos: '+ str(e))


def serial_loop():
    while True:
        if ser.in_waiting > 0:
            reading = ser.read(ser.in_waiting).decode('ascii')
            print(reading)
            if len(reading) > 0:
                save_to_database(reading)
        ser.flush()

def start_serial_loop():
    thread = Thread(target = serial_loop)
    thread.start()