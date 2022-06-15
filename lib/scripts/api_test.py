# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:15:36 2022

@author: HOUJ
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#url = 'https://engine.energytransitionmodel.com/api/v3/areas/BU00141205_hunzepark'
#url = 'https://engine.energytransitionmodel.com/api/v3/scenarios/922908/nodes/buildings_final_demand_electricity'
url = 'https://engine.energytransitionmodel.com/api/v3/scenarios/922908/nodes/buildings_useful_demand_for_space_heating_after_insulation.demand'


headers = {
        'Accepts':'application/json',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)