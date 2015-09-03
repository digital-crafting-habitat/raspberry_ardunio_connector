import redis
import serial

r = redis.StrictRedis(host='85.214.235.74', port=6379, db=0)
ser = serial.Serial('/dev/ttyAMA0', 19200, timeout=100)

if ser.isOpen():
    line = ser.readline()
    line = ser.readline()
    print(int(line.strip()))
    ser.close()
#    print(r.set('value', line))
    if not ser.isOpen():
        print("closed")

print(r.get('foo'))
