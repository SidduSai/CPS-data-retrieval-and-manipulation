from data import MV
from data import FIT

import time

# Add Delay

name = 'CPS_ALID_P1_SD1'

def isViolated():
    mv101 = MV(1, 101)
    fit101 = FIT(1, 101)

    if mv101.isOn:
        time.sleep(4)
        if fit101.value < 0.5:
            return True

    return False