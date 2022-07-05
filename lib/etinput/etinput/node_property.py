from .value import Value

class NodeProperty(Value):
    def __init__(self, key, node_property='.', **kwargs):
        '''Also saves which property of the node is requested'''
        self.node_property = node_property
        super().__init__(key, **kwargs)

    @property
    def node_property(self):
        return self._node_property

    @node_property.getter
    def node_property(self):
        '''Split into the parts needed to traverse the properties dict returned by ETM'''
        return self._node_property.split('.')

    @node_property.setter
    def node_property(self, property_data):
        '''
        We set the full unparsed string here, and only unwrap it when requested.
        A dot '.' should separate the keys in the traversal path.
        E.g. 'technical.electricity_output_conversion.future'.
        '''
        self._node_property = property_data

    def update(self, value):
        '''
        Value is not a single value here, but the full properties dict as returned by the ETM
        We traverse it until we find the correct value.
        '''
        try:
            for key in self.node_property:
                value = value[key]
        except KeyError as err:
            raise UnknownPropertyError(str(err), value, self.key) from err
        finally:
            self._value = float(value)


class UnknownPropertyError(BaseException):
    def __init__(self, key, value, elem, *args):
        message = f'Unknown node property for {elem}: {key} not in {list(value.keys())}'
        super().__init__(message, *args)
