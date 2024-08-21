APP_URL = "https://stellarburgers.nomoreparties.site"
API_URI = f"{APP_URL}/api"


class TestConstants:

    PASSWORD = "P@ssw0rd"

    TEST_USER = {
        "email": "test-op-10@test.host",
        "password": f"{PASSWORD}",
        "name": "test-op-10",
    }

    CORRECT_INGREDIENTS = [
        "61c0c5a71d1f82001bdaaa6d",  # "Флюоресцентная булка R2-D3"
        "61c0c5a71d1f82001bdaaa74",  # "Соус традиционный галактический"
        "61c0c5a71d1f82001bdaaa71",  # "Биокотлета из марсианской Магнолии"
    ]


class Endpoints:
    # fmt: off
    AUTH_LOGIN      = "/auth/login"
    AUTH_LOGOUT     = "/auth/logout"
    AUTH_REGISTER   = "/auth/register"
    AUTH_TOKEN      = "/auth/token"
    AUTH_USER       = "/auth/user"

    INGREDIENTS     = "/ingredients"

    ORDERS          = "/orders"
    ORDERS_ALL      = "/orders/all"

    PASSWORD_RESET  = "/password-reset"
    # fmt: on


class ErrorMessages:
    # auth related
    AUTH_DATA_INCOMPLETE = "Email, password and name are required fields"
    WRONG_AUTH_DATA = "email or password are incorrect"
    USER_EXISTS = "User already exists"
    NEED_AUTHORIZATION = "You should be authorised"

    # orders related
    NO_INGREDIENTS = "Ingredient ids must be provided"
    INCORRECT_INGREDIENTS = "One or more ids provided are incorrect"
