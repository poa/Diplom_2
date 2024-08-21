import pytest
from http import HTTPStatus as HS

from api.orders import OrdersAPI
from const import ErrorMessages as EM


class TestOrdersMake:
    def test_make_authorized_correct_ingredients_successful(self, test_data, user_for_order):
        resp = OrdersAPI.make(test_data.order.correct_ingredients)
        assert resp.status_code == HS.OK and resp.json().get("success", False) is True

    @pytest.mark.parametrize("ingredients", ["no_ingredients", "incorrect_ingredients"])
    def test_make_authorized_wrong_ingredients_unsuccessful(
        self, test_data, user_for_order, ingredients
    ):
        _ingredients = getattr(test_data.order, ingredients)
        _error = getattr(EM, ingredients.upper())
        resp = OrdersAPI.make(_ingredients)
        assert (
            resp.status_code == HS.BAD_REQUEST
            and resp.json().get("success", False) is False
            and resp.json().get("message", False) == _error
        )

    def test_make_authorized_incorrect_ingredient_unsuccessful(self, test_data, user_for_order):
        resp = OrdersAPI.make(test_data.order.no_ingredients)
        assert (
            resp.status_code == HS.BAD_REQUEST
            and resp.json().get("success", False) is False
            and resp.json().get("message", False) == EM.NO_INGREDIENTS
        )

    def test_make_authorized_bad_hash_ingredient_unsuccessful(self, test_data, user_for_order):
        resp = OrdersAPI.make(test_data.order.bad_hash_ingredients)
        assert (
            resp.status_code == HS.INTERNAL_SERVER_ERROR
            and HS.INTERNAL_SERVER_ERROR.phrase in resp.text
        )


class TestOrdersGetForUser:
    def test_get_orders_for_authorized_user_successful(self, test_user_authorized):
        resp = OrdersAPI.get_user_orders(test_user_authorized.access_token)
        assert resp.status_code == HS.OK and resp.json().get("success", False) is True

    def test_get_orders_for_unauthorized_unsuccessful(self, test_user_unauthorized):
        resp = OrdersAPI.get_user_orders(test_user_unauthorized.access_token)
        assert (
                resp.status_code == HS.UNAUTHORIZED
                and resp.json().get("success", False) is False
                and resp.json().get("message") == EM.NEED_AUTHORIZATION
        )
