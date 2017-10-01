from data import MV
from data import LIT
import time

name = 'CPS_ALID_P1_SD3'


def isViolated():
    mv101 = MV(1, 101)
    lit101 = LIT(1, 101)

    if lit101.isHigh:
        time.sleep(10)
        if not mv101.isOff:
            return True

    return False
