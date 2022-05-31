'''
Isto é uma prove of consepct para a nova cabeça de medição de pressão 

mbar default pressure
TODO: Mudar isto para uma class 
'''

import serial
COM = 'COM3'


def Calculate_CS(send_to_head):
    len_msg = 0
    for char in send_to_head:
        # print (ord(char))
        len_msg += ord(char)
    len_msg = (len_msg%64)+64
    return chr(len_msg)

def read_VSR53USB(serial_VSR53USB):
    read_pressor = serial_VSR53USB.read_until(b'\r')
    # print(read_pressor)
    return read_pressor[8:-2]

def int_VSR53USB(COM,Timeout):
    serial_VSR53USB = serial.Serial(COM, timeout=Timeout)
    return serial_VSR53USB

def pressure_Pirani(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'M1'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode())
    
    return read_VSR53USB(serial_VSR53USB)

def pressure_Piezo(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'M2'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode())

    return read_VSR53USB(serial_VSR53USB)


def read_ST(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'ST'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode())
    
    print(read_VSR53USB(serial_VSR53USB))
    return ''


def read_Gas_correctoion(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'C1'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode())
    
    print(read_VSR53USB(serial_VSR53USB))
    return ''

def Adj_Gas_correctoion(serial_VSR53USB,ADR,CR):
    AC = '2'
    CMD = 'C1'
    DATA = '1.0'
    LEN = str(len(DATA))
    if len(LEN) == 1:
        LEN = '0'+LEN
    # print(LEN)
    CS = Calculate_CS(ADR+AC+CMD+LEN+DATA)
    msg = ADR+AC+CMD+LEN+DATA+CS+CR
    
    serial_VSR53USB.write(msg.encode())
    
    print(read_VSR53USB(serial_VSR53USB))
    return ''

def main():
    ADR = '001'
    CR = '\r'
    s = int_VSR53USB('COM3',1)
    print(pressure_Pirani(s,ADR,CR))
    print(pressure_Piezo(s,ADR,CR))
    read_ST(s,ADR,CR)
    Adj_Gas_correctoion(s,ADR,CR)
    read_Gas_correctoion(s,ADR,CR)


main()