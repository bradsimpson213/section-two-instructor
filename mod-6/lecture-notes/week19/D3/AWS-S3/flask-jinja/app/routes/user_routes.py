from flask import Blueprint

from ..models import User

users = Blueprint("users", __name__)

# print("inside users BP", __name__)


@users.route("/")
def user_stuff():
    return "<h2>Users Stuff here!</h2>"


@users.route("/all")
def get_all_user():
    response = [user.to_dict() for user in User.query.all()]
    return {"users": response }