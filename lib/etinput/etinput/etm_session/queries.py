import requests

from .session import ETMSession

class ETMQuerySession(ETMSession):
    ENDPOINT = '/'

    def send_request(self, keys):
        json = { 'scenario': { 'gqueries': keys }}
        yield from self.handle_response(requests.put(self.url(), json=json))

    def handle_response(self, response):
        if response.ok:
            return ((key, values['future']) for key, values in response.json()['gqueries'].items())

        if response.status_code == 422:
            self.fail_with(errors=response.json()['errors'])

        self.fail_with('Something went wrong connecting to the ETM')
