from data import FIT
from data import UV

name = 'CPS_ALID_P4_SD3'


def isViolated():

    fit401 = FIT(4, 401)
    uv401 =  UV(4, 401)

    if fit401.isLowLow and uv401.isOn:
        return True

    return False
