from flask import Flask, request, jsonify
import re

app = Flask(__name__)
users = {}  # email -> {id, password, age}
next_id = 1

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@app.route("/users", methods=["POST"])
def create_user():
    """
    Approach: validate each field independently and return the first
    failure with a specific message (spec requires identifying which
    rule failed, not a generic error). Check uniqueness after format
    validation, since a malformed email shouldn't even reach the
    duplicate check.
    """
    global next_id
    data = request.get_json(silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")
    age = data.get("age")

    if not EMAIL_RE.match(email):
        return jsonify({"error": "invalid email format"}), 400
    if len(password) < 8 or not any(c.isdigit() for c in password):
        return jsonify({"error": "password must be 8+ chars with at least one digit"}), 400
    if not isinstance(age, int) or not (13 <= age <= 120):
        return jsonify({"error": "age must be an integer between 13 and 120"}), 400
    if email in users:
        return jsonify({"error": "email already registered"}), 409

    user_id = next_id
    next_id += 1
    users[email] = {"id": user_id, "password": password, "age": age}
    return jsonify({"id": user_id}), 201
