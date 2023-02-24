from ctypes import ArgumentError
import RPi.GPIO as GPIO
import time
import sys
import serial
import numpy as np
import json
import configparser
import threading

from datetime import datetime

import GPIO as GPIO
import VSR53USB as VSR53USB
import PPT200 as PPT200
from datetime import datetime

OFF = GPIO.OFF
ON = GPIO.ON

presure_new = None
presure_old = None

def Mauser_pressure(old, new):
    global presure_old
    global presure_new
    while True:
        presure_old = "{:.3f}".format(PPT200.get_pressure(old))
        presure_new = new.Pressure()
        time.sleep(0.001)
    return


if __name__ == "__main__":
    status = GPIO.Int_GPIO()
    new_p = VSR53USB.VSR53USB({"COM":'/dev/ttyUSB1',"timeout":1})
    new_p.Adj_Gas_Correctoion_Factor(1)
    old = PPT200.int_com_PPT200('/dev/ttyUSB0')
    data_thread = threading.Thread(target=Mauser_pressure,args=(old,new_p,),daemon=True)
    data_thread.start()
    while True:
        input_msg = input()
        print(input_msg)
        if input_msg == 'vac':
            GPIO.Vacum_Pump_stat(ON)
            time.sleep(2)
            GPIO.Valve_cut_off_stat(ON)
        elif input_msg == 'vacf':
            GPIO.Vacum_Pump_stat(OFF)
            time.sleep(2)
            GPIO.Valve_cut_off_stat(OFF)
        elif input_msg == 'he':
            GPIO.Inject_Gas(1, 10)
        elif input_msg == 'xe':
            GPIO.Inject_Gas(2, 10)
        elif input_msg == 'ar':
            GPIO.Inject_Gas(3, 10)
        elif input_msg == 'cd':
            print("")
        elif input_msg == 'st':
            print("")
        else:
            print(presure_old)
            pass