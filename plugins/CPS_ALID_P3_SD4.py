from data import LIT
from data import Pump, PLC

name = 'CPS_ALID_P3_SD4'

# SD4

# ToDo
# COrrect Invariant Label (name)
# ADd P3_STATE information


def isViolated():

    lit401 = LIT(4, 401)
    lit301 = LIT(3, 301)
    p301 = Pump(3, 301)
    p302 = Pump(3, 302)
    p602 = Pump(6, 602)
    p3 = PLC(3)

    if lit401.isLow and p3.state == 7 and all([p.isOff for p in [p301, p302, p602]]) and p3.isNotOne and p3.state != 99 and not lit301.isLowLow:
        return True

    return False
