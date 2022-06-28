from etinput.etm_session import ETMConnection
from etinput.batch import Batch
from etinput.value import Value

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
