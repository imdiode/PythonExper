import serial
import time

serialPort = serial.Serial('/dev/ttyUSB0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

cmd = bytearray([130,130,82,0,0,0,84,0])

serialPort.write(cmd)

res = serialPort.read(10)