import allure
import requests

from http import HTTPMethod as HM, HTTPStatus as HS


from const import (
    API_URI,
    Endpoints as EP,
)


class AuthAPI:
    def __init__(self, email=None, password=None, name=None):
        self.email = email if email else ""
        self.password = password if password else ""
        self.name = name if name else ""

        self.access_token = None
        self.refresh_token = None

        self.is_registered = False
        self.is_logged_in = False

        self.last_status = None
        self.last_json = {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(
            f" :: On exit delete status for user {self.email}: {self.delete()}: {self.last_json.get("message")}"
        )

    def __update_tokens(self, resp):
        self.access_token = resp.json().get("accessToken")
        self.refresh_token = resp.json().get("refreshToken")

    def __api_req(self, method, endpoint, payload=None, headers=None):
        api = f"{API_URI}{endpoint}"
        req_func = getattr(requests, method.lower())
        resp = req_func(api, headers=headers, json=payload)

        self.last_status = HS(resp.status_code)
        if self.last_status.is_server_error is False:
            self.last_json = resp.json()

        return resp

    @allure.step("Register user")
    def register(self):
        payload = {
            "email": self.email if self.email is not None else "",
            "password": self.password if self.password is not None else "",
            "name": self.name if self.name is not None else "",
        }
        resp = self.__api_req(
            method=HM.POST, endpoint=EP.AUTH_REGISTER, payload=payload
        )

        if self.last_status == HS.OK:
            self.is_registered = True
            self.__update_tokens(resp)

        return self.is_registered

    @allure.step("Login user")
    def login(self, email=None, password=None):
        if self.is_registered:
            payload = {
                "email": email if email is not None else self.email,
                "password": password if password is not None else self.password,
            }
            resp = self.__api_req(
                method=HM.POST, endpoint=EP.AUTH_LOGIN, payload=payload
            )

            if self.last_status == HS.OK:
                self.is_logged_in = True
                self.__update_tokens(resp)

        return self.is_logged_in

    @allure.step("Logout user")
    def logout(self):
        if self.refresh_token is not None:
            payload = {"token": self.refresh_token}
            self.__api_req(method=HM.POST, endpoint=EP.AUTH_LOGOUT, payload=payload)

            if self.last_status == HS.OK:
                self.is_logged_in = False
                self.access_token = None
                self.refresh_token = None
                return True

        return False

    @allure.step("Delete user")
    def delete(self):
        if self.is_registered:
            self.login()
            headers = {"Authorization": f"{self.access_token}"}
            self.__api_req(HM.DELETE, EP.AUTH_USER, headers=headers)

            if self.last_status == HS.ACCEPTED:
                self.is_logged_in = False
                self.is_registered = False
                return True

        return False

    @allure.step("Update user data")
    def update(self, email=None, name=None):
        if self.is_registered:
            headers = {"Authorization": f"{self.access_token}"}
            payload = {}
            if email is not None:
                payload["email"] = email
            if name is not None:
                payload["name"] = name

            self.__api_req(HM.PATCH, EP.AUTH_USER, headers=headers, payload=payload)

            if self.last_status == HS.OK:
                if email is not None:
                    self.email = email
                if name is not None:
                    self.name = name
            return True

        return False
