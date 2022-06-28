class Value:
    def __init__(self, key, endpoint='query', value=None):
        '''Key is the ETM key'''
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
