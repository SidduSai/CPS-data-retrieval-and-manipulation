from data import LIT, FIT
import time

name = 'CPS_ALID_P3_SA1'

FLOW_RATE=0.745712
FLOW_RATE_SEC=0.1864
THRESHOLD = 4.8
CYCLES = 6

def avg(data):
    return float(sum(data))/len(data)

def isViolated():
    lit301 = LIT(3, 301)
    fit201 = FIT(2, 201)
    fit301 = FIT(3, 301)

    closed_errors = []
    open_errors = []

    while True:

        pv = lit301.value
        model_pv = pv

        time.sleep(4)

        closed_pv = pv + (fit201.value - fit301.value)*FLOW_RATE
        pv = lit301.value

        open_pv = model_pv + (fit201.value - fit301.value)*FLOW_RATE
        model_pv = open_pv

        error_closed =  abs(closed_pv - pv)
        error_open  = abs(open_pv - pv)

        closed_errors.append(error_closed)
        open_errors.append(error_open)

        if len(closed_errors) == CYCLES:

            if any(error > THRESHOLD for error in [avg(open_errors), avg(closed_errors)]):
                return True
            else:
                return False

    return True