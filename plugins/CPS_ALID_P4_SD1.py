from data import LIT
from data import Pump

name = 'CPS_ALID_P4_SD1'

import time

def isViolated():

    lit401 = LIT(4, 401)
    p401 = Pump(4, 401)
    p402 = Pump(4, 402)

    if lit401.isLowLow:
        time.sleep(2)
        if any(p.isOn for p in [p401, p402]):
            return True

    return False
