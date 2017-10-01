from data import FIT
from data import Pump
import time

name = 'CPS_ALID_P3_SD2'

#SD2
# Time delay added

def isViolated():

    fit301 = FIT(3, 301)
    p301 = Pump(3,301)

    if p301.isOn:
        time.sleep(4)
        if fit301.value < 0.5:
            return True

    return False
