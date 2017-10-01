from data import AIT
from data import Pump

name = 'CPS_ALID_P2_SD10'


def isViolated():

    ait203 = AIT(2, 203)
    p205 = Pump(2, 205)
    p206 = Pump(2, 206)

    if ait203.isHigh and any(p.isOn for p in [p205,p206]):
        return True

    return False
