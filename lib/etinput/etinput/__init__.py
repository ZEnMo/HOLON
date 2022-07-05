#  Module init
from pathlib import Path
from pydoc import resolve

from etinput.batches import Batches
from etinput.data_requests import DataRequests
from etinput.config import Config

CONFIG_PATH = Path(__file__).parents[1].resolve() / 'config' /'etinput.yml'

def retrieve_results_and_write():
    data_requests = DataRequests.load_from_path(CONFIG_PATH)
    batches = Batches()

    data_requests.ready(batches)
    batches.send()

    destination = Path(Config().output_folder).resolve()
    destination.mkdir(exist_ok=True)
    data_requests.write_to(destination)
