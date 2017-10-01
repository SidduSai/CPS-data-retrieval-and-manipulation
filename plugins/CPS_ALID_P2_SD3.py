from data import FIT
from data import Pump

name = 'CPS_ALID_P2_SD3'

def isViolated():
    fit201 = FIT(2, 201)
    p201 = Pump(2, 201)
    p202 = Pump(2, 202)
    p203 = Pump(2, 203)
    p204 = Pump(2, 204)
    p205 = Pump(2, 205)
    p206 = Pump(2, 206)

    if fit201.isLowLow and any(p.isOn for p in [p201,p202,p203,p204,p205,p206]):
        return True

    return False
