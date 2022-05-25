'''
Isto é uma prove of consepct para a nova cabeça de medição de pressão 

TODO: Mudar isto para uma class 
'''

import serial
COM = 'COM3'


def Calculate_CS(send_to_head):
    len_msg = 0
    for char in send_to_head:
        print (ord(char))
        len_msg += ord(char)
    len_msg = (len_msg%64)+64
    return chr(len_msg)

def int_VSR53USB(COM,Timeout):
    serial_VSR53USB = serial.Serial(COM, timeout=Timeout)
    return serial_VSR53USB

def pressure_Pirani(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'M1'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode('ascii'))
    read_pressor = s.read_until(b'\r')
    return read_pressor

def pressure_Piezo(serial_VSR53USB,ADR,CR):
    AC = '0'
    CMD = 'M2'
    LEN = '00'
    CS = Calculate_CS(ADR+AC+CMD+LEN)
    msg = ADR+AC+CMD+LEN+CS+CR
    
    serial_VSR53USB.write(msg.encode('ascii'))
    read_pressor = s.read_until(b'\r')
    return read_pressor

read_pressor = s.read_until(b'\r')
print(read_pressor)

def main():
    ADR = '001'
    CR = '\r'
    s = int_VSR53USB('COM3',1)
    print(pressure_Pirani(s,ADR,CR))
    print(pressure_Piezo(s,ADR,CR))