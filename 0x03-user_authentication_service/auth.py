#!/usr/bin/env python3
"""This is the Auth Module"""
import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Method that takes in a password string arguments
    and returns bytes.The returned bytes is a salted
    hash of the input password, hashed with bcrypt.hashpw"""
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash
