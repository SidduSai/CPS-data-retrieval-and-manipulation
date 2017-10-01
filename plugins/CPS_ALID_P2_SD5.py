from data import AIT
from data import FIT
from data import Pump
from data import PLC

name = 'CPS_ALID_P2_SD5'


def isViolated():

    ait201 = AIT(2, 201)
    ait503 = AIT(5, 503)
    fit201 = FIT(2, 201)
    p201 = Pump(2, 201)
    p202 = Pump(2, 202)
    p2 = PLC(2)

    if ait201.isLow and not ait503.isHigh and p2.isNotOne and  not fit201.isLow and all(p.isOff for p in [p201, p202]):
        return True

    return False
