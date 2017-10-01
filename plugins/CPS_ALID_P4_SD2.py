from data import FIT
from data import Pump
import time

name = 'CPS_ALID_P4_SD2'

# Delayed Test, add to slower pool

def isViolated():

    fit401 = FIT(4, 401)
    p401 = Pump(4, 401)
    p402 = Pump(4, 402)

    if any(p.isOn for p in [p401, p402]):
    	time.sleep(7)
    	if fit401.value < 0.5:
        	return True

    return False
