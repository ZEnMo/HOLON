from etinput.data_requests import DataRequests
from etinput.single_request import SingleRequest

def test_load():
    data_requests = DataRequests()

    # Check if it has loaded at least one
    assert next(data_requests.all())

    # Is it a request?
    assert isinstance(next(data_requests.all()), SingleRequest)
