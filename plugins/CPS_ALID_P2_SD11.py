from data import AIT, MV, PLC
from data import Pump
import time
name = 'CPS_ALID_P2_SD11'


def isViolated():

    ait203 = AIT(2, 203)
    mv201 = MV(2, 201)
    ait402 = AIT(4, 402)
    p2 = PLC(2)
    p205 = Pump(2, 205)
    p206 = Pump(2, 206)

    if ait203.isLow and mv201.isOn and not ait402.isHigh and p2.isNotOne:
        time.sleep(6)
        if all(p.isOff for p in [p205,p206]) and not mv201.isOff:
            return True

    return False
