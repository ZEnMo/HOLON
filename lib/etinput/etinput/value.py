class Value:
    def __init__(self, key, endpoint='query', value=None):
        '''
        Respresents a value. Values contain info about their ETM key and endpoint,
        and extra information if needed. A (numeric) value is not set at initialisation
        and can be updated after connecting to the ETM.
        '''
        self.key = key
        self.endpoint = endpoint
        self._value = value

    def is_set(self):
        '''Bool, returns if the value is set'''
        if self._value is None:
            return False

        return True

    def update(self, value):
        '''Updates the value'''
        self._value = value

    def write_to(self, path):
        '''Writes the values as a CSV to the given path'''

    def __str__(self):
        return f'{self.__class__.__name__}({self.key})'
