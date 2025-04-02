from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from database import db
from werkzeug.security import generate_password_hash

routes = Blueprint('routes', __name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


@routes.route("/user/signup", methods=["POST"])
def signupUser():
    data = request.get_json()

#  existing_user = User.query.filter_by(email=data["email"]).first()
 #   if existing_user:
  #      return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data["password"])

    # Create new user
    new_user = User(
        name=data["name"],
        password=hashed_password,
        email=data["email"],
        dob=data["dob"],
        phone=data["phone"]
    )

    with db.engine.connect() as connection:
        db.create_all()
        db.session.add(new_user)
        db.session.commit()

    data.pop("password")
    data["user_id"] = new_user.id

    token = create_access_token(identity=str(new_user.id))

    return jsonify({
        "message": "User signed up successfully",
        "user": data,
        "token": token
    }), 201
