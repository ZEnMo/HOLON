from .converter import RequestConverter, MissingRequestInfoException

class SingleRequest(RequestConverter):
    def __init__(self, key, **config_data):
        self.key = key
        self.converter = config_data

    def calculate(self):
        '''Run the converter of the request'''
        self.converter.calculate()

    def values(self):
        yield from self.converter.required_for_calculation()

    def write_to(self, path):
        self.converter.main_value.write_to(path / f'{self.key}.csv')
