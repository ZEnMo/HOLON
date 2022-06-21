import pytest

from etinput.single_request import SingleRequest
from etinput.curve import Curve
from etinput.value import Value
from etinput.converters import DivideBy

@pytest.fixture
def request_with_curve():
    return SingleRequest('buildings_heating_electricity_curve', type='curve',
        etm_key='the_curve_key', conversion='divide', divide_by='the_query_key')

def test_request_with_curve_divide(request_with_curve):
    # Check if the key is set
    assert request_with_curve.key == 'buildings_heating_electricity_curve'

    # Check the values
    values = request_with_curve.values()
    main_value = next(values)
    assert isinstance(main_value, Curve)
    assert main_value.is_set() == False
    assert main_value.key == 'the_curve_key'

    second_value = next(values)
    assert isinstance(second_value, Value)
    assert second_value.is_set() == False
    assert second_value.key == 'the_query_key'

    # Check the converter
    assert request_with_curve.converter
    assert isinstance(request_with_curve.converter, DivideBy)
