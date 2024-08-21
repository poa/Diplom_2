
APP_URL = "https://stellarburgers.nomoreparties.site"
API_URI = f"{APP_URL}/api"


class TestConstants:

    PASSWORD = "P@ssw0rd"

    TEST_USER = {
        "email": "test-op-10@test.host",
        "password": f"{PASSWORD}",
        "name": "test-op-10",
    }


class Endpoints:
    # fmt: off
    INGREDIENTS     = "/ingredients"
    PASSWORD_RESET  = "/password-reset"

    AUTH_LOGIN      = "/auth/login"
    AUTH_LOGOUT     = "/auth/logout"
    AUTH_REGISTER   = "/auth/register"
    AUTH_TOKEN      = "/auth/token"
    AUTH_USER       = "/auth/user"

    ORDERS          = "/orders"
    ORDERS_ALL      = "/orders/all"
    # fmt: on


class ErrorMessages:
    AUTH_DATA_INCOMPLETE = "Email, password and name are required fields"
    WRONG_AUTH_DATA = "email or password are incorrect"
    USER_EXISTS = "User already exists"
    NEED_AUTHORIZATION = "You should be authorised"

