from data import MV, PLC
from data import LIT
import time
name = 'CPS_ALID_P2_SD1'


def isViolated():
    mv201 = MV(2, 201)
    p2 = PLC(2)
    lit301 = LIT(3, 301)

    if lit301.isLow and p2.isNotOne:
    	time.sleep(2)
    	if mv201.isOff:
        	return True

    return False
