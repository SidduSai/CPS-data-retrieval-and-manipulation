from data import Pump
from data import LIT

name = 'CPS_ALID_P1_SD4'


def isViolated():
    p101 = Pump(1, 101)
    p102 = Pump(1, 102)
    lit101 = LIT(1, 101)

    if lit101.isLowLow and any(p.isOn for p in [p101, p102]):
        return True

    return False
