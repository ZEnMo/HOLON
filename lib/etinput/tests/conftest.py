from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from pathlib import Path
import pytest

@pytest.fixture
def config_path():
    return Path('tests/fixtures/etinput_config.yml').resolve()

@pytest.fixture
def nodes_response_data():
    return {
        "technical": {
            "total_installed_electricity_capacity": {
                "present": 5443.360123449158,
                "future": 5443.360123449158,
                "unit": "MW",
                "desc": "Installed electrical capacity"
            },
        },
        "cost": {
            "total_investment_over_lifetime_per_mw_electricity": {
                "present": "958583",
                "future": "958583",
                "unit": "EUR / MW",
                "desc": "Investment over lifetime per MW"
            },
        }
    }

class Helpers:
    '''Put all helper functions that should be globally available here'''
    @staticmethod
    def mock_nodes_response(requests_mock, nodes_response_data, connection, nodes):
        for node in nodes:
            requests_mock.get(
                connection.session.url(node),
                status_code=200,
                json={ "data": nodes_response_data, "key": node }
            )

@pytest.fixture
def helpers():
    '''Namespace the helpers '''
    return Helpers
