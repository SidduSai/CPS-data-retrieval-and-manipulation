from data import DPIT
from data import Pump
import time
name = 'CPS_ALID_P3_SD3'

# ToDo
# SD3

def isViolated():

    dpit301 = DPIT(3, 301)
    p301 = Pump(3, 301)
    p302 = Pump(3, 302)

    if dpit301.isHigh:
	time.sleep(4)
	if any(p.isOn for p in [p301, p302]):
        	return True

    return False
