import random
from pprint import pprint

desc = ["Ask the mighty Kaung", "Ask the mighty Sridhar", "Gyani might know this one"]


super_output = []

def get_lists(plc_no, no_inv):
	output = []

	if plc_no in (1,3,4):
		output.append(
			{
				'tag': 'CPS_ALID_P%d_SA1' %(plc_no),
				'desc': random.choice(desc)
			}
		)

	for i in range(1, no_inv+1):
		output.append(
			{
				'tag': 'CPS_ALID_P%d_SD%d' %(plc_no, i),
				'desc': random.choice(desc)
			}
		)

	super_output.append(output)

	return output

# one SA
pprint(get_lists(1, 7))
pprint(get_lists(2, 13))
# one SA
pprint(get_lists(3,5))
# one SA
pprint(get_lists(4,6))
pprint(get_lists(5,3))
pprint(get_lists(6,3))


pprint(super_output)