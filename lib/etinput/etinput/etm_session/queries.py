import requests

from .session import ETMSession

class ETMQuerySession(ETMSession):
    ENDPOINT = '/'

    def send_request(self, keys):
        json = { 'scenario': { 'gqueries': keys }}
        yield from self._handle_response(requests.put(self.url(), json=json))

    def _handle_response(self, response):
        if response.ok:
            return ((key, values['future']) for key, values in response.json()['gqueries'].items())

        return super()._handle_response(response)
