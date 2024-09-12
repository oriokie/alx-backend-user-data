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


def _generate_uuid() -> str:
    """Method that generates a random UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        """Constructor method for Auth class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new User instance
        Args:
            email: email of user
            password: password of user
        Return:
            User object
        Raise:
            ValueError: if the email already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user
        Args: email (str) and email (str)
        Returns: bool"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a new session for a user
        Args: email(str)
        Returns:
            session_id(str)
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Retrieves a user given a session ID
        Args:
            session_id: the session ID
        Returns:
            User object or None
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys a session for a user
        Args:
            user_id: the user ID
        """
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token
        Args:
            email: the email
        Returns:
            str
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        if user is None:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Updates a user password
        Args:
            reset_token: the reset token
            password: the new password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            user = None
        if user is None:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)
        return None
