import redis
import serial
import time

r = redis.StrictRedis(host='85.214.235.74', port=6379, db=0)
#ser = serial.Serial('/dev/ttyACM0', 19200, timeout=100)
ser = serial.Serial('/dev/tty.usbmodem1451', 9600, timeout=100)

if ser.isOpen():
    line = ser.readline()
    while True:
        time.sleep(1)
        line = ser.readline()
        value = int(line.strip())
        print(value)
        r.set('redstone_value', line)
        if value == 0:
            break
    ser.close()
    if not ser.isOpen():
        print("closed")

print(r.get('foo'))
