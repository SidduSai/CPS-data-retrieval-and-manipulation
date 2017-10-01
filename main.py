from monitor import Monitor
from daemonize import Daemonize
import sys
import coloredlogs
import logging

coloredlogs.install()

logging.getLogger("requests").setLevel(logging.WARNING)


logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}/{1}.log".format(".", "watchman"))
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.WARNING)
rootLogger.addHandler(fileHandler)


def main():

    f = Monitor()

    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        pid = '/tmp/watchman.pid'
        daemon = Daemonize(app='monitoring', pid=pid, action=f.run)
        daemon.start()
    else:
        f.run()

if __name__ == "__main__":
    main()
