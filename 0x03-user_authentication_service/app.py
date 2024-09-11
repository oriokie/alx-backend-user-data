#!/usr/bin/env python3
"""
Flask App that integrates with Auth and DB modules"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Route for creating new users"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return abort(400)
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Login function to respond to the POST /sessions route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return abort(400)
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    return jsonify({"message": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
