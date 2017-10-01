from data import Pump, LIT, AIT, Plant

name = 'CPS_ALID_P6_SD2'


def isViolated():

    lit101 = LIT(1, 101)
    ait202 = AIT(2, 202)
    p601 = Pump(6, 601)
    plant =  Plant()

    if ait202.value >= 7 and not lit101.isHighHigh and p601.isOff and plant.start:
        return True

    return False
