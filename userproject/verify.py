from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

verify_routes = Blueprint('verify_routes', __name__)


@verify_routes.route("/user/verify", methods=["GET"])
@jwt_required()
def verify_user():
    current_user = get_jwt_identity()  # Extract user ID from the token
    return jsonify({
        "message": "User is authorized",
        "user_id": current_user
    }), 200
