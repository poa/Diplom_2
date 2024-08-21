import pytest

from data import TestData

from api.auth import AuthAPI


@pytest.fixture(scope="session")
def test_data():
    data = TestData()
    yield data
    del data


@pytest.fixture(scope="session")
def test_user(test_data):
    with AuthAPI(**test_data.auth.precreated) as test_user:
        test_user.register()
        yield test_user

@pytest.fixture(scope="function")
def test_user_authorized(test_user):
    test_user.login()
    yield test_user


@pytest.fixture(scope="function")
def test_user_unauthorized(test_user):
    test_user.logout()
    yield test_user


@pytest.fixture(scope="function", params=["authorized", "unauthorized"])
def user_for_order(request, test_data):
    fixture = request.getfixturevalue(f"test_user_{request.param}")
    yield fixture
