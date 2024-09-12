#!/usr/bin/env python3
"""This is the main module"""
import requests


# BASE_URL = "http://localhost:5000"
BASE_URL = "http://127.0.0.1:5000"
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Test the register_user route"""
    url = "{}/users".format(BASE_URL)
    body = {"email": email, "password": password}
    response = requests.post(url, data=body)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    response = requests.post(f"{BASE_URL}/sessions",
                             json={"email": email,
                                   "password": password})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    pass


def profile_unlogged() -> None:
    pass


def profile_logged(session_id: str) -> None:
    pass


def log_out(session_id: str) -> None:
    pass


def reset_password_token(email: str) -> str:
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    pass


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
