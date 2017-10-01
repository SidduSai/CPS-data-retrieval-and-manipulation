from data import Pump
from data import FIT
import time

name = 'CPS_ALID_P1_SD7'

# Time delay added

def isViolated():
    p101 = Pump(1, 101)
    p102 = Pump(1, 102)
    fit201 = FIT(2, 201)


    if any(p.isOn for p in [p101, p102]):
        time.sleep(5)
        if fit201.value < 0.5:
            return True
    else:
        time.sleep(5)
        if fit201.value > 0.5:
            return True


    return False
