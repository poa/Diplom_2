from const import TestConstants as TC
from tools import DataGenerator


class AuthData:

    def __init__(self):

        self.precreated = TC.TEST_USER

        data = DataGenerator()

        self.complete = AuthData.get_payload(data.email, TC.PASSWORD, data.name)
        self.no_email = AuthData.get_payload(None, TC.PASSWORD, data.name)
        self.no_password = AuthData.get_payload(data.email, None, data.name)
        self.no_name = AuthData.get_payload(data.email, TC.PASSWORD, None)

    @staticmethod
    def get_payload(email, password, name):
        result = {"email": email, "password": password, "name": name}
        return result


class OrderData:
    def __init__(self):
        self.no_ingredients = []
        self.correct_ingredients = TC.CORRECT_INGREDIENTS
        self.incorrect_ingredients = ["000000000000000000000001"]
        self.bad_hash_ingredients = TC.CORRECT_INGREDIENTS + ["abc123"]


class TestData:
    def __init__(self):
        self.auth = AuthData()
        self.order = OrderData()
