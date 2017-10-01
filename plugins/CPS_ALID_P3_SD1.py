from data import LIT
from data import Pump
import time
name = 'CPS_ALID_P3_SD1'

#SD1

def isViolated():

    lit301 = LIT(3, 301)
    p301 = Pump(3, 301)
    p302 = Pump(3, 302)

    if lit301.isLowLow:
	time.sleep(4)
	if any(p.isOn for p in [p301,p302]):
        	return True

    return False
