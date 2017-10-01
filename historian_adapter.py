from requests.auth import HTTPBasicAuth
from historian.historian import PiWebAPIClient



client = PiWebAPIClient("192.168.1.200", 443, "piwebapi",
                        HTTPBasicAuth("Administrator", "Sutd1234"))

SALL=0
SAL=1
SAH=2
SAHH=3

class DataSource(object):

    def __init__(self, plc, tag):
        self.client = client
        self.plc = plc
        self.tag = tag

    def get(self, var):
        return client.get_current_value("D8CF2232", "SWAT_SUTD:RSLinx Enterprise:P%d.HMI_%s.%s" % (self.plc, self.tag, var))[0]

    def get_bool(self, var):
        return bool(self.get(var)['Value'])


class Numeric(DataSource):

    def __init__(self, plc, subtype, tag):
        super(Numeric, self).__init__(plc, "%s%d" % (subtype, tag))

    @property
    def value(self):
        return float(self.get("Pv"))


    @property
    def isLow(self):
        return self.value <= self.limits[SAL]

    @property
    def isLowLow(self):
        return self.value <= self.limits[SALL]

    @property
    def isHigh(self):
        return self.value >= self.limits[SAH]

    @property
    def isHighHigh(self):
        return self.value >= self.limits[SAHH]


class Boolean(DataSource):

    def __init__(self, plc, subtype, tag):
        super(Boolean, self).__init__(plc, "%s%d" % (subtype, tag))

    @property
    def isOn(self):
        return self.get("Status") == 2

    @property
    def isOff(self):
        return self.get("Status") == 1

# Correct this

class PLC():

    def __init__(self, plc):
        self.plc = plc
        self.client = client

    @property
    def state(self):
        return client.get_current_value("D8CF2232", "SWAT_SUTD:RSLinx Enterprise:P%d.HMI_P%d_STATE" %(self.plc, self.plc))[0]

    @property
    def isNotOne(self):
        return self.state !=1
    @property
    def isOne(self):
        return not self.isNotOne

class Plant():

    def __init__(self):
        self.client = client

    @property
    def start(self):
        return bool(client.get_current_value("D8CF2232", "SWAT_SUTD:RSLinx Enterprise:P1.HMI_PLANT.START")[0]['Value'])
    @property
    def stop(self):
        return not self.start

class LIT(Numeric):

    def __init__(self, plc, tag):
        super(LIT, self).__init__(plc, "LIT", tag)

        if plc == 1:
            self.limits = [250, 500, 800, 1000]
        elif plc == 3:
            self.limits = [250, 800, 1000, 1198]
        elif plc == 4:
            self.limits = [250, 800, 1000, 1100]

class AIT(Numeric):

    def __init__(self, plc, tag):
        super(AIT, self).__init__(plc, "AIT", tag)

        if plc == 2:
            if tag == 201:
                self.limits = [50, 250, 260, 950]
            elif tag == 202:
                self.limits = [3.00, 6.95, 7.05, 12.00]
            elif tag == 203:
                self.limits = [100, 440, 480, 750]
        elif plc == 4:
            if tag == 401:
                self.limits = [0, 0, 80, 100]
            elif tag == 402:
                self.limits = [200, 250, 300, 800]
        elif plc == 5:
            if tag == 501:
                self.limits = [0]*4
            elif tag == 502:
                self.limits = [0, 0, 250, 300]
            elif tag == 504:
                self.limits = [0, 0, 30, 35]
            elif tag == 503:
                self.limits = [0, 250, 260, 500]

class FIT(Numeric):

    def __init__(self, plc, tag):
        super(FIT, self).__init__(plc, "FIT", tag)

        if tag == 101:
            self.limits = [0.5, 1.0, 3.0, 4.0]
        elif tag == 201:
            self.limits = [0.0, 0.0, 2.5, 3.0]
        elif tag == 301:
            self.limits = [0, 0, 3, 3.5]
        elif tag == 401:
            self.limits = [0.5, 1.0, 2.0, 3.0]
        elif tag == 501:
            self.limits = [0, 1, 2, 3]
        elif tag == 502:
            self.limits = [0]*4
        elif tag == 503:
            self.limits = [0]*4
        elif tag == 504:
            self.limits = [0, 0, 1.0, 3.5]


class Pump(Boolean):

    def __init__(self, plc, tag):
        super(Pump, self).__init__(plc, "P", tag)


class MV(Boolean):

    def __init__(self, plc, tag):
        super(MV, self).__init__(plc, "MV", tag)


class PSH(Numeric):

    def __init__(self, plc, tag):
        super(PSH, self).__init__(plc, "PSH", tag)


class DPIT(Numeric):

    def __init__(self, plc, tag):
        super(DPIT, self).__init__(plc, "DPIT", tag)

        if tag == 301:
            self.limits = [10, 15, 40, 100]


class DPSH(Numeric):

    def __init__(self, plc, tag):
        super(DPSH, self).__init__(plc, "DPSH", tag)


class UV(Boolean):

    def __init__(self, plc, tag):
        super(UV, self).__init__(plc, "UV", tag)
