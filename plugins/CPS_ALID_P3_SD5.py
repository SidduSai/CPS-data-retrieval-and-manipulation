from data import LIT
from data import Pump

name = 'CPS_ALID_P3_SD5'

# SD5

def isViolated():

    lit401 = LIT(4, 401)
    p301 = Pump(3, 301)
    p302 = Pump(3, 302)

    if lit401.isHigh and any(p.isOn for p in [p301, p302]):
        return True

    return False
