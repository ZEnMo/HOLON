from etinput.data_requests import DataRequests
from etinput.single_request import SingleRequest
# TODO: should point this to a fixture
from etinput import CONFIG_PATH
from etinput.batches import Batches

def test_load():
    data_requests = DataRequests.load_from_path(CONFIG_PATH)

    # Check if it has loaded at least one
    assert next(data_requests.all())

    # Is it a request?
    assert isinstance(next(data_requests.all()), SingleRequest)

def test_ready_batches():
    data_requests = DataRequests.load_from_path(CONFIG_PATH)
    batches = Batches()

    # Quick check up front
    for batch in batches.each():
        assert batch.is_empty()

    # Ready them
    data_requests.ready(batches)

    # Is there something in them now?
    for batch in batches.each():
        if batch.endpoint == 'nodes': continue # Not yet implemented

        assert not batch.is_empty()
