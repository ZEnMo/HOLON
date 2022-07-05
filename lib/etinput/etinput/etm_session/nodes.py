import requests

from .session import ETMSession

class ETMNodesSession(ETMSession):
    ENDPOINT = '/nodes/'

    def send_request(self, keys):
        '''Multiple requests - one for each key. Yields the results (key, value pairs) one by one'''
        for key in keys:
            yield (key, self._handle_response(requests.get(self.url(key))))

    def url(self, key=''):
        return f'{super().url()}{key}'

    def _handle_response(self, response):
        '''
        We filter the data only when updating the Value. Hence we send the whole object as result
        '''
        if response.ok:
            return response.json()['data']

        return super()._handle_response(response)
