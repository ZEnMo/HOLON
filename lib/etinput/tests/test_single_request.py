import pytest

from etinput.single_request import SingleRequest
from etinput.curve import Curve

@pytest.fixture
def request_with_curve():
    return SingleRequest('buildings_heating_electricity_curve', type='curve',
        etm_key='the_curve_key', conversion='divide', divide_by='the_query_key')

def test_request_with_curve_divide(request_with_curve):
    # CHeck if all correct attributes are set
    assert request_with_curve.key == 'buildings_heating_electricity_curve'
    assert isinstance(request_with_curve.value, Curve)
    assert request_with_curve.value.is_set() == False
    assert request_with_curve.value.key == 'the_curve_key'

    # TODO: continue here next time
    # assert request_with_curve.converter
    # assert isinstance(request_with_curve.converter, DivideBy)
