import pytest
from http import HTTPStatus as HS

from api.auth import AuthAPI
from const import ErrorMessages as EM


class TestAuthRegister:
    def test_register_complete_data_successful(self, test_data):
        with AuthAPI(**test_data.auth.complete) as user:
            user.register()
            assert user.last_status == HS.OK and user.last_json.get("success") is True

    @pytest.mark.parametrize("auth_params", ["no_email", "no_password", "no_name"])
    def test_register_incomplete_data_unsuccessful(self, test_data, auth_params):
        auth_data = getattr(test_data.auth, auth_params)
        with AuthAPI(**auth_data) as user:
            user.register()
            assert (
                user.last_status == HS.FORBIDDEN
                and user.last_json.get("success") is False
                and user.last_json.get("message") == EM.AUTH_DATA_INCOMPLETE
            )

    def test_register_existing_user_unsuccessful(
        self, test_data, test_user_unauthorized
    ):
        with AuthAPI(**test_data.auth.precreated) as user:
            user.register()
            assert (
                user.last_status == HS.FORBIDDEN
                and user.last_json.get("success") is False
                and user.last_json.get("message") == EM.USER_EXISTS
            )


class TestAuthLogin:
    def test_login_correct_data_successful(self, test_user_unauthorized):
        test_user_unauthorized.login()
        assert (
            test_user_unauthorized.last_status == HS.OK
            and test_user_unauthorized.last_json.get("success") is True
            and test_user_unauthorized.last_json.get("accessToken") is not None
        )

    @pytest.mark.parametrize(
        "wrong_attr",
        [{"email": "new_email_123@test.host"}, {"password": "1qaz.2wsx.3edc"}],
    )
    def test_login_wrong_data_unsuccessful(self, test_user_unauthorized, wrong_attr):
        test_user_unauthorized.login(**wrong_attr)
        assert (
            test_user_unauthorized.last_status == HS.UNAUTHORIZED
            and test_user_unauthorized.last_json.get("success") is False
            and test_user_unauthorized.last_json.get("message") == EM.WRONG_AUTH_DATA
        )


class TestAuthUpdate:
    @pytest.mark.parametrize(
        "updated_attr",
        [{"email": "new_email_123@test.host"}, {"name": "new_user_name"}],
    )
    def test_update_authorized_successful(self, test_data, updated_attr):
        with AuthAPI(**test_data.auth.complete) as user:
            user.register()
            user.login()
            user.update(**updated_attr)
            returned_attr_value = user.last_json.get("user").get(
                str(*updated_attr.keys())
            )
            assert (
                user.last_status == HS.OK
                and user.last_json.get("success") is True
                and returned_attr_value == str(*updated_attr.values())
            )

    @pytest.mark.parametrize(
        "updated_attr",
        [{"email": "new_email_123@test.host"}, {"name": "new_user_name"}],
    )
    def test_update_unauthorized_unsuccessful(
        self, test_user_unauthorized, updated_attr
    ):
        test_user_unauthorized.update(**updated_attr)
        assert (
            test_user_unauthorized.last_status == HS.UNAUTHORIZED
            and test_user_unauthorized.last_json.get("success") is False
            and test_user_unauthorized.last_json.get("message") == EM.NEED_AUTHORIZATION
        )
