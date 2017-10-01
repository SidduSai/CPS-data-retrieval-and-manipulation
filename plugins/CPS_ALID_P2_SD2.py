from data import MV
from data import LIT

name = 'CPS_ALID_P2_SD2'

import time

def isViolated():
    mv201 = MV(2, 201)
    lit301 = LIT(3, 301)

    if lit301.isHigh:
        time.sleep(2)
        if mv201.isOn:
            return True

    return False
