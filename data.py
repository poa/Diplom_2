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
        data = DataGenerator()

        complete_set_base = [
            data.first_name,
            data.last_name,
            data.address,
            data.metro_station,
            data.phone,
            data.rent_period_int,
            data.date,
            data.comment,
        ]

        self.complete_set_no_color = complete_set_base + [None]
        self.complete_set_black_color = complete_set_base + [TC.SCOOTER_COLORS[0]]
        self.complete_set_grey_color = complete_set_base + [TC.SCOOTER_COLORS[1]]
        self.complete_set_both_color = complete_set_base + [TC.SCOOTER_COLORS]


class TestData:
    def __init__(self):
        self.auth = AuthData()
        # self.order = OrderData()
