from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

hello_routes = Blueprint('hello_routes', __name__)


@hello_routes.route("/hello", methods=["GET"])
@jwt_required()
def hello():
    current_user = get_jwt_identity()  # Get user ID from token
    return jsonify({
        "message": "Hello, World!",
        "user_id": current_user
    }), 200
