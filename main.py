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
Stp = True
print_out = False

f = None

def Mauser_pressure(old, new):
    global presure_old
    global presure_new
    while True:
        presure_old = "{:.3f}".format(PPT200.get_pressure(old))
        presure_new = new.Pressure()
        if print_out:
            print(float(presure_old)*100)
        time.sleep(0.001)
    return

def Save_data(f):
    global presure_old
    global presure_new
    global Stp
    while Stp:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\t"+str(float(presure_old)*100)+"\t"+str(float(presure_new.decode('ascii'))*100)+"\n")
        time.sleep(2)
    return

def init_save_file():
    f = open("Comperation_gauge.txt", "w")
    f.write("Time\tPressure Old [Pa]\tPressure New [Pa]\n")
    f.flush()
    return f


if __name__ == "__main__":
    status = GPIO.Int_GPIO()
    new_p = VSR53USB.VSR53USB({"COM":'/dev/ttyUSB2',"timeout":1})
    new_p.Adj_Gas_Correctoion_Factor(1)
    old = PPT200.int_com_PPT200('/dev/ttyUSB0')
    data_thread = threading.Thread(target=Mauser_pressure,args=(old,new_p,),daemon=True)
    data_thread.start()
    f = init_save_file()
    data_collection = threading.Thread(target=Save_data,args=(f,),daemon=True)
    
    while True:
        print(presure_old)
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
            time_s = input()
            GPIO.Inject_Gas(1, int(time_s))
        elif input_msg == 'xe':
            time_s = input()
            GPIO.Inject_Gas(2, int(time_s))
        elif input_msg == 'ar':
            time_s = input()
            GPIO.Inject_Gas(3, int(time_s))
        elif input_msg == 'so':
            print_out = True
        elif input_msg == 'sf':
            print_out = False
        elif input_msg == 'cd':
            data_collection.start()
        elif input_msg == 'st':
            Stp = False
            time.sleep(1)
            print("Closing file!\n\r")
            f.flush()
            f.close()
        else:
            pass