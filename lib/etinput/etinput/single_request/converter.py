from etinput.curve import Curve
from etinput.value import Value
import etinput.converters as converters

class RequestConverter:
    @property
    def converter(self):
        return self._converter

    @converter.setter
    def converter(self, config):
        # TODO: Add validation!! What if these are not in the kwargs etc
        self._converter = self._create_converter(
            self._main_value(config.pop('etm_key'), config.pop('type')),
            config
        )

    # Private

    def _main_value(self, etm_key, data_type):
        '''
        Extract which type of data we're dealing with, can be a Curve or a single value
        '''
        if data_type == "curve":
            return Curve(etm_key)
        else:
            return Value(etm_key)

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
        if conversion == 'divide' and 'divide_by' in converter_config:
            return converters.DivideBy(main_value, Value(converter_config.pop('divide_by')))

        raise MissingRequestInfoException(f'Missing info for request {self.key}')


class MissingRequestInfoException(BaseException):
    pass
