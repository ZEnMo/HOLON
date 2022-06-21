import requests
from .config import Config

class ETMSession:
    def __init__(self, key):
        '''Do requests to the endpoint named by the key'''
        self.key = key

    def send_request(self, keys):
        '''Return or yield (?) maybe better to yield when they turn out not to be doable in batches'''
        request_type = Config().endpoints[self.key]['type']

        if request_type == 'get':
            # TODO: continue here, make some nice requests and monkeypatches -> curves can't be in
            # batches, neither can't nodes - so their results should be saved or better yielded to
            # the batch
            self.handle_response(requests.get(self.url(), params=keys))
        elif request_type == 'put':
            json = { 'scenario': { 'gqueries': keys }}
            yield from self.handle_response(requests.put(self.url(), json=json))
        # else:
        #     # raise something

    def handle_response(self, request):
        '''Return the handled response (list/dict of outcomes)'''
        #  TODO: Do we make sub classes to handle the different endpoints in the end?
        pass

    def url(self):
        return Config().api_url + Config().scenario.id + Config().endpoints[self.key]['endpoint']
