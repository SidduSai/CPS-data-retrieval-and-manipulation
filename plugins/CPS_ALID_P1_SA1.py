from data import LIT, FIT
import time

name = 'CPS_ALID_P1_SA1'

FLOW_RATE=0.745712
THRESHOLD = 5.5
CYCLES = 6

def avg(data):
    return float(sum(data))/len(data)

def isViolated():
    lit101 = LIT(1, 101)
    fit201 = FIT(2, 201)
    fit101 = FIT(1, 101)

    closed_errors = []
    open_errors = []

    while True:

        pv = lit101.value
        model_pv = pv

        time.sleep(4)

        closed_pv = pv + (fit101.value - fit201.value)*FLOW_RATE
        pv = lit101.value

        open_pv = model_pv + (fit101.value - fit201.value)*FLOW_RATE
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