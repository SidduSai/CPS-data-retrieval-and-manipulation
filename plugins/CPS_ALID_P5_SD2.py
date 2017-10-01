from data import UV
from data import Pump
import time

name = 'CPS_ALID_P5_SD2'


def isViolated():

    uv401 = UV(4, 401)
    p501 = Pump(5, 501)
    p502 = Pump(5, 502)

    if uv401.isOff:
        time.sleep(2)
        if any(p.isOn for p in [p501, p502]):
            return True

    return False
