import requests

from http import HTTPStatus as HS

from const import (
    API_URI,
    Endpoints as EP,
)


class IngredientsAPI:
    @staticmethod
    def get_ingredients():
        api = f"{API_URI}{EP.INGREDIENTS}"
        resp = requests.get(api)

        if resp.status_code == HS.OK and resp.json().get("success", False) is True:
            return resp.json().get("data")
        else:
            return []
