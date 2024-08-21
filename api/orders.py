import allure
import requests

from const import (
    API_URI,
    Endpoints as EP,
)


class OrdersAPI:
    @staticmethod
    @allure.step("Make order")
    def make(ingredients=None):
        if ingredients is None:
            ingredients = []
        payload = {"ingredients": ingredients}
        api_url = API_URI + EP.ORDERS
        resp = requests.post(api_url, json=payload)

        return resp

    @staticmethod
    @allure.step("Get user orders")
    def get_user_orders(access_token=""):
        api_url = API_URI + EP.ORDERS
        headers = {"Authorization": f"{access_token}"}

        resp = requests.get(api_url, headers=headers)

        return resp
