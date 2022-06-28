from .batch import Batch
from .value import Value
from .curve import Curve

class Batches:
    def __init__(self):
        self._curves = Batch('curves')
        self._nodes = Batch('nodes')
        self._queries = Batch('queries')

    def each(self):
        yield self._curves
        yield self._nodes
        yield self._queries

    def add(self, value):
        '''Adds a Value to the correct Batch'''
        if value.endpoint == 'curve':
            self._curves.add(value)
        elif value.endpoint == 'query':
            self._queries.add(value)
        # elif isinstance(value, NodeProperty):
        #     self._nodes.add(value)
        else:
            raise UnknownValueType(f'The object {value} could not be added to a batch')

    def send(self):
        '''Sends all the batches'''
        for batch in self.each():
            batch.send()

class UnknownValueType(BaseException):
    pass
