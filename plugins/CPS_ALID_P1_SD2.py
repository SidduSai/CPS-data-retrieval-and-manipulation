from data import MV
from data import LIT
import time

name = 'CPS_ALID_P1_SD2'


def isViolated():
    mv101 = MV(1, 101)
    lit101 = LIT(1, 101)

    if lit101.isLow:
        time.sleep(10)
        if not mv101.isOn:
            return True

    return False
