import yaml
from datetime import *
from threading import Thread
import time

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

if config["web"]["enabled"] == True:
    from library.web import http
    #http.run(config)


def logger(config):
    while True:
        time.sleep(5.5)
        with open(config["general"]["logfile"], 'a') as log:
            log.write("{0},{1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str('asda')))

t = Thread(target=logger, args=(config,))
t.start()

print('poo')
