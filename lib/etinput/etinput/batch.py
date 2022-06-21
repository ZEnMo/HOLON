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

    def inject_results(self, results):
        '''Update the Values with the results from the response'''
