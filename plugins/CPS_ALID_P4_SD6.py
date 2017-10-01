from data import AIT
from data import Pump, PLC

name = 'CPS_ALID_P4_SD6'


def isViolated():

    ait402 = AIT(4, 402)
    p403 = Pump(4, 403)
    p404 = Pump(4, 404)
    p4 = PLC(4)

    if ait402.isHigh and any(p.isOff for p in [p403, p404]) and p4.state == 4:
        return True

    return False
