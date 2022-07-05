from etinput.etm_session import ETMConnection
from etinput.batch import Batch
from etinput.value import Value
from etinput.node_property import NodeProperty


def test_send_batch(requests_mock):
    endpoint = 'queries'
    batch = Batch(endpoint)

     # QUERIES
    requests_mock.put(
        ETMConnection(endpoint).session.url(),
        status_code=200,
        json={
            "gqueries": {
                "costs_of_insulation": {
                    "present": 0.0,
                    "future": 1234567.8,
                    "unit": "euro"
                },
                "costs_of_capital_in_electricity_production": {
                    "present": 1234567.8,
                    "future": 2345678.9,
                    "unit": "euro"
                }
            }
        }
    )

    value_1 = Value("costs_of_insulation")
    value_2 = Value("costs_of_capital_in_electricity_production")
    batch.add(value_1, value_2)

    batch.send()

    assert value_1.is_set()
    assert value_2.is_set()

def test_send_batch_to_nodes(requests_mock, nodes_response_data, helpers):
    endpoint = 'nodes'
    batch = Batch(endpoint)
    nodes = ['industry_chp_combined_cycle_gas_power_fuelmix', 'node_2']
    helpers.mock_nodes_response(requests_mock, nodes_response_data, ETMConnection(endpoint), nodes)

    value_1 = NodeProperty(
        "industry_chp_combined_cycle_gas_power_fuelmix",
        'technical.total_installed_electricity_capacity.future',
        endpoint='node_property'
    )
    value_2 = NodeProperty(
        "node_2",
        'cost.total_investment_over_lifetime_per_mw_electricity.future',
        endpoint='node_property')
    batch.add(value_1, value_2)

    batch.send()

    assert value_1.is_set()
    assert value_2.is_set()

    assert value_1._value == 5443.360123449158
    assert value_2._value == 958583
