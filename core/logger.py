import time
import datetime
from threading import Thread

def logthread(config):
    while True:
        time.sleep(config["poll_interval"])
        with open(config["logfile"], 'a') as log:
            log.write("{0},{1}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(config["command"])))

def log(config):
    t = Thread(target=logthread, args=(config,))
    t.start()
