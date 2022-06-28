from .queries import ETMQuerySession
from .curves import ETMCurvesSession
from .nodes import ETMNodesSession

class ETMConnection:
    def __init__(self, endpoint_key):
        '''Connect to the endpoint named by the key'''
        self.session = endpoint_key

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, endpoint_key):
        '''Sets the correct session based on the endpoint_key'''
        if endpoint_key == 'queries':
            self._session = ETMQuerySession()
        elif endpoint_key == 'curves':
            self._session == ETMCurvesSession()
        elif endpoint_key == 'nodes':
            self._session = ETMNodesSession()
        else:
            raise InvalidEndpoint(endpoint_key)

    def connect(self, requested_keys):
        '''
        Connect to the ETM through the ETMSession session, and yield the results
        of the response.

        Params:
            requested_keys(List[str]): A list of keys to request to the endpoint

        Returns:
            Generator[(str, float)] of results (key value pairs)
        '''
        yield from self.session.send_request(requested_keys)


class InvalidEndpoint(BaseException):
    def __init__(self, endpoint, *args):
        mess = f'No method available to connect to endpoint {endpoint}'
        super().__init__(mess, *args)
