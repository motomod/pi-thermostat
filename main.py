import yaml
from core import logger
from web import http


with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

logger.log(config["temp"])





http.run(config["web"])
print('poo')
