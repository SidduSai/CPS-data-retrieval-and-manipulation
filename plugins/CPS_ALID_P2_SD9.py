from data import AIT, FIT, MV
from data import Pump, PLC
import time
name = 'CPS_ALID_P2_SD9'


def isViolated():

    ait202 = AIT(2, 202)
    p203 = Pump(2, 203)
    p204 = Pump(2, 204)
    p2 = PLC(2)
    fit201 = FIT(2, 201)
    mv201 = MV(2, 201)

    if ait202.isHigh and p2.isNotOne and not fit201.isLow and mv201.isOn:
        time.sleep(6)
        if all(p.isOff for p in [p203,p204]) and not fit201.isLow and mv201.isOn:
            return True

    return False
