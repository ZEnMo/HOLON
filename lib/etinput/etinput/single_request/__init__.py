from .converter import RequestConverter

class SingleRequest(RequestConverter):
    def __init__(self, key, **config_data):
        self.key = key
        self.converter = config_data

    def update(self, data):
        '''Updates the current value(s) of the request with ETM data'''
        # And starts the calculator?

    def values(self):
        yield from self.converter.required_for_calculation()

    def write_to(self, path):
        self.value.write_to(path)
