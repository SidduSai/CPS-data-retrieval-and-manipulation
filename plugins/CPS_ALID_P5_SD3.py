from data import Pump, FIT

name = 'CPS_ALID_P5_SD3'


def isViolated():

    fit401 = FIT(4, 401)
    p501 = Pump(5, 501)
    p502 = Pump(5, 502)

    if fit401.isLowLow and any(p.isOn for p  in [p501,p502]):
        return True

    return False
