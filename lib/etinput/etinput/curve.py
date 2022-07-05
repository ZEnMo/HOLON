import numpy as np

from etinput.value import Value


class Curve(Value):
    def __init__(self, key, endpoint='query', value=np.array(0)):
        '''Values should be an np.array of 8760 - add validations'''
        super().__init__(key, endpoint=endpoint, value=value)

    def is_set(self):
        '''Bool, returns if the value is set'''
        if self._value.size == 1:
            return False

        return True

    def update(self, array):
        '''Updates the value'''
        self._value = np.array(array)

    def divide_by(self, other):
        '''Divides itself by the other Value, validates this Value is not zero'''
        if other._value == 0:
            return

        self._value = self._value / other._value

    def sum(self):
        '''Only used for validation'''
        return self._value.sum()

    # Later we can add other actions like summing curves, multiplying, etc. We can move
    # them to a module 'operations' when there are starting to be too many

    def _value_as_np(self):
        return self._value
