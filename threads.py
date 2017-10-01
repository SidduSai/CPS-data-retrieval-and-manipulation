from threading import Thread
import logging
from datetime import datetime as dt

DATA_EXPIRATION_SECONDS=120

class SuperThread(Thread):

    def __init__(self, plugin, redis):
        Thread.__init__(self)
        self.daemon = True
        self.plugin = plugin
        self.redis = redis
        self.setName(plugin.name)
        self.start()

    def run(self):
        while True:
            self.check_and_raise_alert()

    def check_and_raise_alert(self):
        isViolated = self.plugin.isViolated()
        self.redis.set(self.plugin.name, isViolated)
        self.redis.expire(self.plugin.name, DATA_EXPIRATION_SECONDS)
        self.redis.set('%s:timestamp' % self.plugin.name, dt.now())
        if isViolated:
            logging.warn("[%s] VIOLATED" % self.plugin.name)
        else:
            logging.info("[%s] SAFE" % self.plugin.name)
