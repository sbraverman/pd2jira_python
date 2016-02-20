import os
import yaml

class Configs(object):

    @staticmethod
    def get():
        file_name = os.path.join(os.path.dirname(__file__), 'configs.yml')
        with open(file_name, 'r') as configs:
            return yaml.load(configs) 
