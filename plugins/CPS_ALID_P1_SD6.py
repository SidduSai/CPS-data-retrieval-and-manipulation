from data import Pump
from data import LIT

name = 'CPS_ALID_P1_SD6'


def isViolated():
    p101 = Pump(1, 101)
    p102 = Pump(1, 102)
    lit301 = LIT(3, 301)

    if lit301.isHigh and any(p.isOn for p in[p101, p102]):
        return True

    return False
