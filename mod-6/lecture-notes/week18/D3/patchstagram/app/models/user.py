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

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profilePic": self.profile_pic,
            "bio": self.bio,
            "posts": [post.to_dict_no_user() for post in self.posts],
            "likes": len(self.user_likes)
        }
    
    def to_dict_no_post(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profilePic": self.profile_pic,
            "bio": self.bio,
            "likes": len(self.user_likes)
        }