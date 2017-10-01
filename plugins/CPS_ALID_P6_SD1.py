from data import Pump, LIT, AIT

name = 'CPS_ALID_P6_SD1'


def isViolated():

    lit101 = LIT(1, 101)
    ait202 = AIT(2, 202)
    p601 = Pump(6, 601)

    if lit101.isHighHigh and ait202.value < 7 and p601.isOn:
        return True

    return False
