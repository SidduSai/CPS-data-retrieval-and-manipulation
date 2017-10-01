from data import AIT
from data import Pump

name = 'CPS_ALID_P2_SD8'


def isViolated():

    ait202 = AIT(2, 202)
    p203 = Pump(2, 203)
    p204 = Pump(2, 204)

    if ait202.value < 6.95 and any(p.isOn for p in [p203, p204]):
        return True

    return False
