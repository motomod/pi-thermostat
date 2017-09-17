import yaml

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

if config["web"]["enabled"] == True:
    from library.web import http
    http.run(config)
