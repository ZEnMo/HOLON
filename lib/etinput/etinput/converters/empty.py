from .base import BaseConverter

class Empty(BaseConverter):
    '''Converter that does not convert anything'''
    def __init__(self, main_value):
        self.main_value = main_value

    def required_for_calculation(self):
        '''Generator, returns all Values that should be arequested from the ETM'''
        yield self.main_value
