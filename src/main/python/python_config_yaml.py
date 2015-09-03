import yaml

with open("../resources/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg['arduino'])
test = cfg['arduino']['values'][1]