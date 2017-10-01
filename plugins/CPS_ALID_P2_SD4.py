from data import AIT
from data import Pump

name = 'CPS_ALID_P2_SD4'


def isViolated():
    ait201 = AIT(2, 201)
    p201 = Pump(2, 201)
    p202 = Pump(2, 202)

    if ait201.isHigh and any(p.isOn for p in [p201, p202]):
        return True

    return False
