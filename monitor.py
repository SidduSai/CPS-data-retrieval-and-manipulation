import redis
from extensions import extension_loader
import logging
from threads import SuperThread

class Monitor:

    def __init__(self, run_forever=True):
        self.run_forever = run_forever
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.load_plugins()
        logging.info("System is Running")

    def load_plugins(self):
        self.plugins = extension_loader()

    def run_plugins(self):
        for plugin in self.plugins:
            logging.debug("Creating Thread for %s"%(plugin.name))
            t = SuperThread(plugin, self.redis)

    def run(self):
        self.run_plugins()
        while True:
            pass