import pytest

from etinput.batches import Batches
from etinput.curve import Curve
from etinput.value import Value

@pytest.fixture
def values():
    return [Value('query_one'), Curve('interconnector_price_curve')]

def test_add_values(values):
    batches = Batches()
    print(values)

    # Are they all valid?
    for batch in batches.each():
        assert batch.is_empty()

    # Let's add some things
    for value in values:
        batches.add(value)

    # Is there something in them?
    for batch in batches.each():
        if batch.endpoint == 'nodes': continue # Not yet implemented

        assert not batch.is_empty()
