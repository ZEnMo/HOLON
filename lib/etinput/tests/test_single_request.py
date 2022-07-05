import pytest
import numpy as np

from etinput.single_request import SingleRequest, MissingRequestInfoException
from etinput.curve import Curve
from etinput.value import Value
from etinput.converters import DivideBy
from etinput.node_property import NodeProperty

@pytest.fixture
def request_with_curve():
    return SingleRequest('buildings_heating_electricity_curve', value={'data':'curve',
        'etm_key':'the_curve_key', 'type':'query'}, conversion='divide',
        convert_with_value={'data':'curve', 'etm_key':'the_query_key', 'type':'query'})

@pytest.fixture
def request_with_curve_and_node_property():
    return SingleRequest('buildings_heating_electricity_curve', value={'data':'curve',
        'etm_key':'the_curve_key', 'type':'query'}, conversion='divide',
        convert_with_value={'data':'technical.electricity_output_conversion.future',
        'etm_key':'industry_chp_combined_cycle_gas_power_fuelmix', 'type':'node_property'})

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


def test_calculate(request_with_curve):
    # Set some values
    request_with_curve.converter.main_value.update(np.ones(8760))
    request_with_curve.converter.second_value.update(2)

    request_with_curve.calculate()

    # Did the converter run?
    assert request_with_curve.converter.main_value.sum() == 8760 / 2

def test_request_with_curve_and_node_property(request_with_curve_and_node_property):
    # Check if the key is set
    assert request_with_curve_and_node_property.key == 'buildings_heating_electricity_curve'

     # Check the values
    values = request_with_curve_and_node_property.values()
    main_value = next(values)
    assert isinstance(main_value, Curve)
    assert main_value.is_set() == False
    assert main_value.key == 'the_curve_key'

    second_value = next(values)
    assert isinstance(second_value, NodeProperty)
    assert second_value.is_set() == False
    assert second_value.key == 'industry_chp_combined_cycle_gas_power_fuelmix'

    # Check the converter
    assert request_with_curve_and_node_property.converter
    assert isinstance(request_with_curve_and_node_property.converter, DivideBy)


def test_request_without_correct_value_properties():
    # With just one value with typos - this is OK here, it will probably mess up
    # somewhere in the batches
    SingleRequest('some_key', value={'data':'curves',
        'etm_key':'the_curve_key', 'type':'query'})

    # With one value with 'type' missing
    with pytest.raises(MissingRequestInfoException):
        SingleRequest('some_key', value={'data':'curve',
            'etm_key':'the_curve_key'})

    # With an unknown conversion
    with pytest.raises(MissingRequestInfoException):
        SingleRequest('buildings_heating_electricity_curve', value={'data':'curve',
            'etm_key':'the_curve_key', 'type':'query'}, conversion='kittens',
            convert_with_value={'data':'curve', 'etm_key':'the_query_key', 'type':'query'})

    # With a conversion that takes a second value, where this value is not specified
    with pytest.raises(MissingRequestInfoException):
        SingleRequest('buildings_heating_electricity_curve', value={'data':'curve',
            'etm_key':'the_curve_key', 'type':'query'}, conversion='divide')
