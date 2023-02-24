from ctypes import ArgumentError
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ON = 1
OFF = 0

pressure = 0
serial_pressure = None
Valve_cut_off = 23  # will be 13 but for now is the 23 because we only have a valvu
Vacum_Pump=12
Discharge=5
Helio = 17
Argon = 22
Xenon = 27
Magnite_on = 6
Magnite_1 = 26
Magnite_2 = 16



def Int_GPIO():
    GPIO.setup(Valve_cut_off, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Vacum_Pump, GPIO.OUT, initial=GPIO.HIGH)
    
    
    GPIO.setup(Helio, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Argon, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Xenon, GPIO.OUT, initial=GPIO.HIGH)
    
    GPIO.setup(Discharge, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Magnite_on, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Magnite_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Magnite_2, GPIO.OUT, initial=GPIO.HIGH)
    return True

def Discharge_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Discharge, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Discharge, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return

def Magnite_on_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Magnite_on, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Magnite_on, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return


def Magnite_1_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Magnite_1, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Magnite_1, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return

def Magnite_2_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Magnite_2, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Magnite_2, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return

def Vacum_Pump_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Vacum_Pump, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Vacum_Pump, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return

def Valve_cut_off_stat(ON_OFF):
    if int(ON_OFF) == 1:
        GPIO.output(Valve_cut_off, GPIO.LOW)
    elif int(ON_OFF) == 0:
        GPIO.output(Valve_cut_off, GPIO.HIGH)
    else:
        print("ERROR on the Discharge")
    return

def Inject_Gas(gas_type, injection_time):
    if gas_type == 1:
        # print("\n\n\n\n\n\n\n\n\n\n\nAOQOQO\n\n\n\n\n\n\n\n\n")
        Gas = Helio
    elif gas_type == 3:
        Gas = Argon
    elif gas_type == 2:
        Gas = Xenon
    else:
        print("ERRO: Gas selector!")
    GPIO.output(Gas, GPIO.LOW)
    time.sleep(0.001*int(injection_time))
    GPIO.output(Gas, GPIO.HIGH)
    return