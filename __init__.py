from data import *

def all(variables, value):
    for var in variables:
        if var != value:
            return False
    return True

def not_all(variables, value):
	return not all(variables, value)

ait201 = AIT(2, 201)
p201 = Pump(2, 201)
p203 = Pump(2, 203)