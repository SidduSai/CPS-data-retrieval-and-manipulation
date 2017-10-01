from data import AIT, FIT
from data import Pump
import time
name = 'CPS_ALID_P2_SD7'


def isViolated():

    ait503 = AIT(5, 503)
    fit201 = FIT(2, 201)
    p201 = Pump(2, 201)
    p202 = Pump(2, 202)

    if not ait503.isHigh and not fit201.isLowLow:
        time.sleep(2)
        if all(p.isOff for p in [p201, p202]):
            return True

    return False
