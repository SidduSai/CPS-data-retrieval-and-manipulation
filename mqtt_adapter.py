import paho.mqtt.client as mqtt


class DataSource(object):

    def __init__(self, topic):
        self.topic = topic
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.ip)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe(self.topic)

    def __del__(self):
        self.client.loop_stop()


class Numeric(DataSource):

    def __init__(self, topic):
        self._value = None
        self.ip = "10.0.1.187"
        super(Numeric, self).__init__(topic)

    def on_message(self, dummy, userdata, msg):
        self._value = float(msg.payload)

    @property
    def value(self):
        return self._value

    @property
    def isLow(self):
        return self.value < self.sal

    @property
    def isLowLow(self):
        return self.value < self.sall

    @property
    def isHigh(self):
        return self.value > self.sah

    @property
    def isHighHigh(self):
        return self.value > self.sahh

class LIT(Numeric):

    def __init__(self, plc, tag):

        super(LIT, self).__init__("/swat/plc%d/AI/level" % (plc))
        self.sal = 500
        self.sall = 250
        self.sah = 800
        self.sahh = 1000

# Set Correct SAL SAH

class FIT(Numeric):

    def __init__(self, plc, tag):

        super(FIT, self).__init__("/swat/plc%d/AI/flow" % (plc))
        self.sal = 500
        self.sall = 250
        self.sah = 800
        self.sahh = 1000

class AIT(Numeric):

    def __init__(self, plc, tag):


        if tag == 201:
            topic = "/swat/plc%d/AI/raw_water_conductivity" %(plc)
        elif tag == 202:
            topic = "/swat/plc%d/AI/raw_water_pH" %(plc)
        elif tag == 203:
            topic = "/swat/plc%d/AI/raw_water_ORP" %(plc)
        elif tag == 501:
            topic = "/swat/plc%d/AI/RO_feed_water_conductivity" %(plc)
        elif tag == 502:
            topic = "/swat/plc%d/AI/RO_feed_water_pH" %(plc)
        elif tag == 503:
            topic = "/swat/plc%d/AI/RO_feed_water_ORP" %(plc)
        elif tag == 504:
            topic = "/swat/plc%d/AI/RO_permeate_conductivity" %(plc)



        super(AIT, self).__init__(topic)
        self.sal = 500
        self.sall = 250
        self.sah = 800
        self.sahh = 1000
