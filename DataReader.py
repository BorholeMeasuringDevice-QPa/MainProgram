import serial

# funkcja odczytująca dane z Arduino
def data_reader():
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    s = [0, 1]
    while True:
        read_serial = ser.readline()
        s[0] = ser.readline()
        print(s[0])
        print(read_serial)
    return 0