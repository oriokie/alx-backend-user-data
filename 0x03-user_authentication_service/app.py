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
        return jsonify({"email": user.email, "message": "user created"}), 200
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout function to respond to the DELETE /sessions route"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile() -> str:
    """Profile function to respond to the GET /profile route"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """Reset password function to respond to the POST /reset_password route"""
    email = request.form.get('email')
    if email is None:
        return abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        return jsonify({"message": "email not registered"}), 403


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """Update password function to respond to the PUT /reset_password route"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    if email is None or reset_token is None or new_password is None:
        return abort(403)
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        return jsonify({"message": "Invalid reset token"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
