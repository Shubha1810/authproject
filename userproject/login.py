from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from database import db
from signup import User
from werkzeug.security import check_password_hash

login_routes = Blueprint('login_routes', __name__)


@login_routes.route("/user/login", methods=["POST"])
def loginUser():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({"error": "No user found"}), 404

    if not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200
