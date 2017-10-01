from data import Pump
import time
name = 'CPS_ALID_P5_SD1'


def isViolated():

    p401 = Pump(4, 401)
    p501 = Pump(5, 501)

    if p401.isOff:
        time.sleep(4)
        if p501.isOn:
            return True

    return False
