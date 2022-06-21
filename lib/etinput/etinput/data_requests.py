import yaml

from .single_request import SingleRequest

class DataRequests:
    def __init__(self, single_requests):
        self.data_requests = single_requests

    def all(self):
        '''Generates all requests for parsing'''
        yield from self.data_requests

    def ready(self, batches):
        '''Sort the values from the requests in batches for the endpoints'''
        for single_request in self.all():
            for value in single_request.values():
                batches.add(value)

    def convert(self):
        '''Start converters on all single_requests'''
        for request in self.all():
            request.calculate()

    def write_to(self, path):
        '''Tell all single requests to start writing their data'''
        for request in self.all():
            request.write_to(path)

    @classmethod
    def load_from_path(cls, path):
        '''Loads the data requests from the config'''
        with open(path, 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)

        return cls([SingleRequest(key, **data) for key, data in doc.items()])
