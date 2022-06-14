import numpy as np

from etinput.value import Value


class Curve(Value):
    def __init__(self, key, value=np.array(0)):
        '''Values should be an np.array of 8760 - add validations'''
        super().__init__(key, value=value)

    def is_set(self):
        '''Bool, returns if the value is set'''
        if self._value.size == 1:
            return False

        return True

    def update(self, array):
        '''Updates the value'''
        # self._value = array

    def divide_by(self, other):
        '''Divides itself by the other Value, validate value is not zero, etc'''

    # Later we can add other actions like summing curves, multiplying, etc.

    def write_to(self, path):
        '''Writes the values as a CSV to the given path'''
        # Validate if value is set!!
