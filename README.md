# Pressure Reading

This project started as a repository for the python code that reads out the pressure readings from the VSR53USB.

However, it has been extended to calculate the readings taken by the PPT200 and VSR53USB using a Rasberry Pi to control the injection of a gas and the vacuum cut-off valve and pump ([GPIO](Libs\GPIO.py)).

The code for the two gauges can be found in the Libs folder. 

For the PPT200 you will need to install (https://pypi.org/project/pfeiffer-vacuum-protocol/):

```
    pip install pfeiffer-vacuum-protocol
```

And for the VSR53USB you will need to install the:

```
    pip install pyserial
```


