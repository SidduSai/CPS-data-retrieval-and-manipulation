from data import AIT
from data import Pump

name = 'CPS_ALID_P2_SD6'


def isViolated():
    ait503 = AIT(5, 503)
    p201 = Pump(2, 201)
    p202 = Pump(2, 202)

    if ait503.isHigh and any(p.isOn for p in [p201, p202]):
        return True

    return False
