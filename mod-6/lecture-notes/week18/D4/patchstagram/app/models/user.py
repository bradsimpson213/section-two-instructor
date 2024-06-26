from .db import db
from .likes import likes


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    profile_pic = db.Column(db.String(250))
    bio = db.Column(db.String(255))

    posts = db.relationship("Post", back_populates="user")
    user_likes = db.relationship(
        "Post",
        secondary=likes,
        back_populates='post_likes',
    )

