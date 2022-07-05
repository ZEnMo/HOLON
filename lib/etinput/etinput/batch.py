from etinput.etm_session import ETMConnection

class Batch():
    def __init__(self, endpoint):
        '''
        Create a batch request

        Params:
            endpoint: Valid endpoint of the ETM, can be one of 'curves', 'nodes' or 'queries'
        '''
        self.endpoint = endpoint
        self._batch = []

    def is_empty(self):
        '''Returns if the batch is empty or not'''
        return len(self._batch) == 0

    def add(self, *values):
        '''Add one or more Values to the batch'''
        for value in values:
            self._batch.append(value)

    def keys(self):
        '''Returns a list of keys that should be requested from the endpoint'''
        return [value.key for value in self._batch]

    def send(self):
        '''Create ETM session with the config stuff and send and handle results'''
        if not self._batch: return

        self._inject_results(ETMConnection(self.endpoint).connect(self.keys()))

    # Private

    def _inject_results(self, results):
        '''Update the Values in the batch with the results from the response'''
        for key, new_value in results:
            self._search(key).update(new_value)

    def _search(self, key):
        '''Search for a Value in the batch, used for updating'''
        for value in self._batch:
            if value.key == key:
                return value

        raise KeyError(f'Could not find {key} in batch {self.endpoint}')
