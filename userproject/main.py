from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from signup import routes, User
from login import login_routes
from hello import hello_routes
from verify import verify_routes  # Import verify_routes
from database import db

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(routes)
app.register_blueprint(login_routes)
app.register_blueprint(hello_routes)
app.register_blueprint(verify_routes)  # Register verify_routes


@app.route("/user/<int:user_id>", methods=["GET"])
@jwt_required()  # Requires authentication
def get_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "dob": user.dob,
        "phone": user.phone
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
