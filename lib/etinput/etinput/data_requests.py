from pathlib import Path
import yaml

from .single_request import SingleRequest

class DataRequests:
    CONFIG_PATH = Path(__file__).parents[1].resolve() / 'config' /'etinput.yml'

    def __init__(self):
        self.data_requests = self._load()

    def all(self):
        '''Generates all requests for parsing'''
        yield from self.data_requests

    def ready_requests(self):
        '''Retrieve all neccesary queries and endpoints and make them in a nice format'''

    def update_info(self, info):
        '''Update all data_requests'''

    # Private

    def _load(self):
        '''Loads the data requests from the config'''
        with open(self.CONFIG_PATH, 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)

        return [SingleRequest(key, **data) for key, data in doc.items()]
