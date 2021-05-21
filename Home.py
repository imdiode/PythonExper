import serial
#linux
#serialPort = serial.Serial('/dev/ttyUSB0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
#windows
#serialPort = serial.Serial('COM3', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
gcmd = bytearray([130,130,82,0,0,0,84,0])
dcmd = bytearray([130,130,82,12,0,0,84,12])

while True:
    serialPort.write(gcmd)
    res = serialPort.read(10)
    pv = bytearray([res[0], res[1]])
    sv = bytearray([res[2], res[3]])
    pvint = int.from_bytes(pv, "little", signed="True")
    svint = int.from_bytes(sv, "little", signed="True")
    serialPort.write(dcmd)
    res = serialPort.read(10)
    decimal = bytearray([res[6], res[7]])
    decimalint = int.from_bytes(decimal, "little", signed="True")
    divs = pow(10, decimalint)
    pvfl = pvint/pow(10, decimalint)
    svfl = svint/pow(10, decimalint)

    print(str(pvfl) + ", " + str(svfl))