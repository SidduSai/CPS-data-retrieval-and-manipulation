DB = 'HISTORIAN'

if DB == 'HISTORIAN':
    from historian_adapter import *
elif DB == 'MQTT':
	from mqtt_adapter import *