'''
Singleton class containing the main config
'''

import yaml
from pathlib import Path

class Config:
    CONFIG_PATH = Path(__file__).parents[1].resolve() / 'config' / 'config.yml'

    class __Config:
        def __init__(self, data):
            self.data = data

    instance = None
    def __init__(self):
        if not Config.instance:
            Config.instance = Config.__Config(self._load())

    def __getattr__(self, key):
        return self.instance.data.get(key, None)

    # TODO: parse the Scenario

    def _load(self):
        with open(self.CONFIG_PATH, 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)

        return doc
