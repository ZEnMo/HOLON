from etinput.curve import Curve
from etinput.value import Value

class SingleRequest:
    def __init__(self, key, **kwargs):
        self.key = key

        #  Add validation!!
        self.value = self._get_value(kwargs.pop('etm_key'), kwargs.pop('type'))
        self.converter = self._get_converter(kwargs)


    def update(self, data):
        '''Updates the current value(s) of the request with ETM data'''


    def write_to(self, path):
        self.value.write_to(path)

    # Private

    def _get_value(self, etm_key, data_type):
        '''
        Extract which type of data we're dealing with, can be a Curve or a single value
        '''
        if data_type == "curve":
            return Curve(etm_key)
        else:
            return Value(etm_key)

    def _get_converter(self, converter_info):
        # Set the converter and any additional value needed (e.g. DivideBy)
        pass
