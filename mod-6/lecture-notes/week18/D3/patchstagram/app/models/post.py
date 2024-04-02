from .db import db
from .likes import likes


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    image = db.Column(db.String(255), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    user = db.relationship("User", back_populates="posts")
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates='user_likes',
    )


    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
           
       }


    #  def to_dict(self, user=False):
    #     data = {
    #         "id": self.id,
    #         "caption": self.caption,
    #         "image": self.image,
    #         "postDate": self.post_date,
   
    #     }
    #     if user == True:
    #         data["user"] = self.user.to_dict_no_post()
            
    #     return data

    def to_dict_no_user(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "likes": len(self.post_likes)
       }
