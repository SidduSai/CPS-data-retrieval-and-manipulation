from influxdb import InfluxDBClient

client = InfluxDBClient('10.0.1.187', 8086, 'admin', 'admin', 'swat')


class Numeric(object):

    def __init__(self):
        self.client = client

    def get(self, query):
        return self.client.query(query)[0]['last']

    @property
    def value(self):
        return self.get(self.value_query)

    @property
    def value_query(self):
        return "select last(value) from mqtt_consumer_plc%dDIAI where topic='%s'"%(self.plc, self.tag)

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


class Boolean(object):

    def __init__(self):
        self.client = client

    def get(self, query):
        return self.client.query(query)

    @property
    def isOn(self):
        return bool(self.get(self.on_query)[0])

    @property
    def isOff(self):
        return not self.isOn


class LIT(Numeric):

    def __init__(self, plc):

        super(LIT, self).__init__()

        self.tag = "/swat/plc%d/AI/level" %(plc)
        self.sal = 500
        self.sall = 250
        self.sah = 800
        self.sahh = 1000


class AIT(Numeric):

    def __init__(self, plc):

        super(LIT, self).__init__()

        self.tag = "/swat/plc%d/AI/level" %(plc)
        self.sal = 500
        self.sall = 250
        self.sah = 800
        self.sahh = 1000