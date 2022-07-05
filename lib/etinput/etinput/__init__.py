#  Module init
from pathlib import Path

from etinput.batches import Batches
from etinput.data_requests import DataRequests
from etinput.config import Config

CONFIG_PATH = Path(__file__).parents[1].resolve() / 'config' /'etinput.yml'

def retrieve_results():
    data_requests = DataRequests.load_from_path(CONFIG_PATH)
    batches = Batches()

    data_requests.ready(batches)
    batches.send()
    data_requests.write_to(Config().output_folder)
