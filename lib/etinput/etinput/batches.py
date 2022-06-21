from .batch import Batch
from .value import Value
from .curve import Curve

class Batches:
    def __init__(self):
        # TODO: do we want more endpoint info (like full endpoint including scenario)?
        self._curves = Batch('curves')
        self._nodes = Batch('nodes')
        self._queries = Batch('queries')

    def each(self):
        yield self._curves
        yield self._nodes
        yield self._queries

    def add(self, value):
        '''Adds a Value to the correct Batcht'''
        if isinstance(value, Curve):
            self._curves.add(value)
        elif isinstance(value, Value):
            self._queries.add(value)
        # elif isinstance(value, NodeProperty):
        #     self._nodes.add(value)
        else:
            raise UnknownValueType(f'The object {value} could not be added to a batch')

class UnknownValueType(BaseException):
    pass
