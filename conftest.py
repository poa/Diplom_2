import pytest

from data import TestData

from api.auth import AuthAPI


@pytest.fixture(scope="function")
def test_data():
    data = TestData()
    yield data
    del data


@pytest.fixture(scope="function")
def test_user_authorized(test_data):
    with AuthAPI(**test_data.auth.precreated) as test_user:
        test_user.register()
        test_user.login()
        yield test_user


@pytest.fixture(scope="function")
def test_user_unauthorized(test_data):
    with AuthAPI(**test_data.auth.precreated) as test_user:
        test_user.register()
        test_user.logout()
        yield test_user
