import datetime
import redis

# assuming rs is your redis connection
def is_redis_available(rs):
    # ... get redis connection here, or pass it in. up to you.
    try:
        rs.get(None)  # getting None returns None or throws an exception
    except (redis.exceptions.ConnectionError,
            redis.exceptions.BusyLoadingError):
        return False
    return True

invariant_tags =[
 [{'desc': 'LIT101 state estimation', 'tag': 'CPS_ALID_P1_SA1'},
  {'desc': 'MV101 is OPEN => FIT101 > delta', 'tag': 'CPS_ALID_P1_SD1'},
  {'desc': 'LIT101 is LOW => MV101 is OPEN', 'tag': 'CPS_ALID_P1_SD2'},
  {'desc': 'LIT101 is HIGH => MV101 is CLOSE', 'tag': 'CPS_ALID_P1_SD3'},
  {'desc': 'LIT101 is LOW LOW => P101 | P102 ARE OFF', 'tag': 'CPS_ALID_P1_SD4'},
  {'desc': 'LIT301 is LOW => P101 | P102 ARE ON', 'tag': 'CPS_ALID_P1_SD5'},
  {'desc': 'LIT301 High => P101 | P102 OFF', 'tag': 'CPS_ALID_P1_SD6'},
  {'desc': 'P101 | P102 ON => FIT201 > delta', 'tag': 'CPS_ALID_P1_SD7'}],

 [{'desc': 'LIT301  Low => MV201 Open', 'tag': 'CPS_ALID_P2_SD1'},
  {'desc': 'LIT301 High => MV201 close', 'tag': 'CPS_ALID_P2_SD2'},
  {'desc': 'FIT201 Low Low => P201, P202, P203, P204, P205, P206 OFF', 'tag': 'CPS_ALID_P2_SD3'},
  {'desc': 'AIT201 (High) > 260 uS/cm => P201 | P202 OFF', 'tag': 'CPS_ALID_P2_SD4'},
  {'desc': 'AIT201  < 250 uS/cm => P201 | P202 ON', 'tag': 'CPS_ALID_P2_SD5'},
  {'desc': 'AIT503 HIGH => P201 | P202 OFF', 'tag': 'CPS_ALID_P2_SD6'},
  {'desc': 'AIT503 NOT HIGH => P201 | P202 ON', 'tag': 'CPS_ALID_P2_SD7'},
  {'desc': 'AIT202 <6.95 => P203 | P204 OFF', 'tag': 'CPS_ALID_P2_SD8'},
  {'desc': 'AIT202 > 7.05 => P203 | P204 ON', 'tag': 'CPS_ALID_P2_SD9'},
  {'desc': 'AIT203 HIGH => P205 | P206 OFF', 'tag': 'CPS_ALID_P2_SD10'},
  {'desc': 'AIT203 LOW => P205 | P206 ON', 'tag': 'CPS_ALID_P2_SD11'},
  {'desc': 'AIT402 HIGH => P205 | P206 OFF', 'tag': 'CPS_ALID_P2_SD12'},
  {'desc': 'AIT402 NOT HIGH => P205 | P206 ON', 'tag': 'CPS_ALID_P2_SD13'}],

 [{'desc': 'LIT301 <= Low Low => P301 | P302 OFF', 'tag': 'CPS_ALID_P3_SA1'},
  {'desc': 'P301 ON => FIT301 > delta', 'tag': 'CPS_ALID_P3_SD1'},
  {'desc': 'PSH301, DPIT301, DPSH301 > threshold => P301 OFF', 'tag': 'CPS_ALID_P3_SD2'},
  {'desc': 'LIT401 Low => P301 | P302 ON', 'tag': 'CPS_ALID_P3_SD3'},
  {'desc': 'LIT401 High => P301 | P302 OFF', 'tag': 'CPS_ALID_P3_SD4'},
  {'desc': 'LIT301 state estimation', 'tag': 'CPS_ALID_P3_SD5'}],

 [{'desc': 'LIT401 state estimation', 'tag': 'CPS_ALID_P4_SA1'},
  {'desc': 'LIT401 <= Low Low => P401 | P402 OFF', 'tag': 'CPS_ALID_P4_SD1'},
  {'desc': 'P401 | P402 ON => FIT401 > delta', 'tag': 'CPS_ALID_P4_SD2'},
  {'desc': 'FIT401 Low Low => UV401 OFF', 'tag': 'CPS_ALID_P4_SD3'},
  {'desc': 'P401 OFF => UF401 OFF', 'tag': 'CPS_ALID_P4_SD4'},
  {'desc': 'AIT402 Low => P403 | P404 OFF', 'tag': 'CPS_ALID_P4_SD5'},
  {'desc': 'AIT402 High => P403 | P404 ON', 'tag': 'CPS_ALID_P4_SD6'}],

 [{'desc': 'P401 OFF => P501 OFF', 'tag': 'CPS_ALID_P5_SD1'},
  {'desc': 'UV401 OFF => P501 OFF', 'tag': 'CPS_ALID_P5_SD2'},
  {'desc': 'FIT401 Low Low => P501 OFF', 'tag': 'CPS_ALID_P5_SD3'}],

 [{'desc': 'LIT101 HH & AIT202.Pv < 7 => P601 OFF', 'tag': 'CPS_ALID_P6_SD1'}]
]


def get_status(plc):

	if plc < 1 or plc > 7:
		return False

	try:
		result = []
		if plc==7:
			tags = []

			for t in invariant_tags:
				tags.extend(t)
		else:
			tags = invariant_tags[plc-1]

		client = redis.StrictRedis(host='localhost', port=6379, db=0)

		if is_redis_available(client):
			for tag in tags:
				try:
					if client.get(tag['tag']) =='True':
						status = 'Violated'
						color = 'card hoverable dapp-card red accent-3 blink'
					elif client.get(tag['tag']) == 'False':
						status = 'Not Violated'
						color = 'card hoverable dapp-card light-green accent-3'
					else:
						status = 'Tag not found'
						color = 'card hoverable dapp-card grey darken-2 white-text'
				except:
					status = 'Tag Not Found'
					color = 'card hoverable dapp-card grey darken-2 white-text'

				result.append(
					{
						'name': tag['tag'],
						'status': status,
						'color': color,
						'desc': tag['desc'],
						'updated_at': client.get('%s:timestamp' % tag['tag'])
					}
				)

		else:
			for tag in tags:
				result.append({
					'name': tag['tag'],
					'status': 'Couldnt Connect',
					'color': 'card hoverable dapp-card grey darken-3 accent-3',
					'desc': tag['desc'],
					'updated_at': datetime.datetime.now()
				})
		return result

	except:
		if plc == 7:
			tags = []

			for t in invariant_tags:
				tags.extend(t)
		else:
			tags = invariant_tags[plc-1]
		result = []
		for tag in tags:
			result.append({
				'name': tag['tag'],
				'status': 'Host Unreachable',
				'color': 'card hoverable dapp-card grey darken-4 white-text',
				'desc': tag['desc'],
				'updated_at': datetime.datetime.now()
			})

		return result
