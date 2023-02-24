'''
Isto é uma prove of consepct para a nova cabeça de medição de pressão 

mbar default pressure
TODO: Mudar isto para uma class 
'''

import serial



class VSR53USB:
    '''
    Correction factor C1 Pirani:

    Ar  |  1.6
    CO  |  1.0
    CO2 |  0.89
    H2  |  0.57
    He  |  1.0
    N2  |  1.0
    Ne  |  1.4
    Kr  |  2.4

    '''
    Ar = '1.6' # 1
    He = '1.0' # 2
    Ne = '1.4' # 3

    Data_Correction = { "1": Ar,
                        "2": He,
                        "3": Ne
    }


    ADR = '001'
    CR = '\r'

    def __init__(self,varia):
        self.serial_COM = self.int_VSR53USB(varia["COM"],varia["timeout"])
        return  

    def int_VSR53USB(self,COM,Timeout):
        serial_VSR53USB = serial.Serial(COM, timeout=Timeout)
        return serial_VSR53USB
       

    def Calculate_CS(self,send_to_head):
        len_msg = 0
        for char in send_to_head:
            # print (ord(char))
            len_msg += ord(char)
        len_msg = (len_msg%64)+64
        return chr(len_msg)

    def read_VSR53USB(self):
        read_pressor = self.serial_COM.read_until(b'\r')
        # print(read_pressor)
        return read_pressor[8:-2]

    def Adj_Gas_Correctoion_Factor(self,Gas_type):
        AC = '2'
        CMD = 'C1'
        DATA = self.Data_Correction[str(Gas_type)]
        LEN = str(len(DATA))
        if len(LEN) == 1:
            LEN = '0'+LEN
        # print(LEN)
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN+DATA)
        msg = self.ADR+AC+CMD+LEN+DATA+CS+self.CR
        
        self.serial_COM.write(msg.encode())
        print(self.read_VSR53USB())
        return ''

    def Read_Gas_Correctoion(self):
        AC = '0'
        CMD = 'C1'
        LEN = '00'
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN)
        msg = self.ADR+AC+CMD+LEN+CS+self.CR
        
        self.serial_COM.write(msg.encode())
        
        print(self.read_VSR53USB())
        return ''

    def Pressure_Pirani(self):
        AC = '0'
        CMD = 'M1'
        LEN = '00'
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN)
        msg = self.ADR+AC+CMD+LEN+CS+self.CR
        
        self.serial_COM.write(msg.encode())
        
        return self.read_VSR53USB()

    def Pressure_Piezo(self):
        AC = '0'
        CMD = 'M2'
        LEN = '00'
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN)
        msg = self.ADR+AC+CMD+LEN+CS+self.CR
        
        self.serial_COM.write(msg.encode())

        return self.read_VSR53USB()

    def Pressure(self):
        AC = '0'
        CMD = 'MV'
        LEN = '00'
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN)
        msg = self.ADR+AC+CMD+LEN+CS+self.CR
        
        self.serial_COM.write(msg.encode())

        return self.read_VSR53USB()


    def Read_Sensor_Transition(self):
        AC = '0'
        CMD = 'ST'
        LEN = '00'
        CS = self.Calculate_CS(self.ADR+AC+CMD+LEN)
        msg = self.ADR+AC+CMD+LEN+CS+self.CR
        
        self.serial_COM.write(msg.encode())
        
        print(self.read_VSR53USB())
        return ''

def main():
    VSR53 = VSR53USB({"COM":'/dev/ttyUSB1',"timeout":1})
    VSR53.Adj_Gas_Correctoion_Factor(1)
    print(VSR53.Pressure_Pirani())
    print(VSR53.Pressure_Piezo())
    print(VSR53.Pressure())
    VSR53.Read_Sensor_Transition()
    VSR53.Read_Gas_Correctoion()


main()
