from data import UV
from data import Pump, PLC
import time
name = 'CPS_ALID_P4_SD4'


def isViolated():

    p401 = Pump(4, 401)
    p402 = Pump(4, 402)
    uv401 = UV(4, 401)
    p4 = PLC(4)

    if all(p.isOff for p in [p401,p402]) and p4.state == 4:
        time.sleep(3)
        if uv401.isOn:
            return True

    return False
