from data import AIT, PLC, FIT, MV
from data import Pump
import time

name = 'CPS_ALID_P2_SD13'


def isViolated():

    ait402 = AIT(4, 402)
    p2 = PLC(2)
    fit201 = FIT(2, 201)
    p205 = Pump(2, 205)
    p206 = Pump(2, 206)
    mv201 = MV(2, 201)

    if not ait402.isHigh and p2.isNotOne and not fit201.isLow:
        time.sleep(6)
        if all(p.isOff for p in [p205, p206]) and not fit201.isLowLow and not mv201.isOff:
            return True

    return False
