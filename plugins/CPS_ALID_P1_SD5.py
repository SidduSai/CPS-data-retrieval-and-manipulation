from data import Pump, PLC
from data import LIT
import time

name = 'CPS_ALID_P1_SD5'


def isViolated():
    p101 = Pump(1, 101)
    p102 = Pump(1, 102)
    lit301 = LIT(3, 301)
    p1 = PLC(1)

    if lit301.isLow and p1.isNotOne:
        time.sleep(12)
        if all(p.isOff for p in [p101, p102]):
            return True

    return False
