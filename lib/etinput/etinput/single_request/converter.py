from etinput.curve import Curve
from etinput.value import Value
from etinput.node_property import NodeProperty
import etinput.converters as converters

class RequestConverter:
    @property
    def converter(self):
        return self._converter

    @converter.setter
    def converter(self, config):
        # TODO: Add validation!! What if these are not in the kwargs etc
        self._converter = self._create_converter(
            self._as_value(config.pop('value')),
            config
        )

    # Private

    def _as_value(self, value_data):
        '''Unpacks data and returns a Value based on it'''
        return self._value_for(value_data['etm_key'], value_data['data'], value_data['type'])

    def _value_for(self, etm_key, data, endpoint):
        '''
        Extract which type of data we're dealing with, can be a Curve or a single value
        '''
        if data == "curve":
            return Curve(etm_key, endpoint)
        elif endpoint == "node_property":
            return NodeProperty(etm_key, node_property=data, endpoint=endpoint)
        else:
            return Value(etm_key, endpoint)

    def _create_converter(self, main_value, converter_config):
        '''
        Set the converter and any additional value needed (e.g. DivideBy)

        Assumes the divide_by is not another curve, just a query!

        Params:
            main_value(Value):          The Value that should be converted
            converter_config(kwargs):   Has at least the key 'conversion'. Used to determine the
                                        converter for this data request.
        '''
        conversion = converter_config.pop('conversion')
        if conversion == 'divide' and 'convert_with_value' in converter_config:
            return converters.DivideBy(
                main_value,
                self._as_value(converter_config.pop('convert_with_value'))
            )

        raise MissingRequestInfoException(f'Missing info for request {self.key}')


class MissingRequestInfoException(BaseException):
    pass
