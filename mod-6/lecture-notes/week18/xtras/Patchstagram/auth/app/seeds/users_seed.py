from app.models import db, User
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash


def seed_users():

    user1 = User(
            username="Patchenator",
            email="patch_the_cat@gmail.com",
            password="i_luv_fud",
            profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg",
            bio= "I love naps and food",
    )

    user2 = User(
            username="Blueberry44",
            email="blue@aol.com",
            password="catNinja",
            profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912128/Patchstagram/66346842095__0566A55A-DF10-4E86-A59A-F5694436FA4E_wmoi1w.jpg",
            bio="I am a ninja! 🥷🏻",
    )

    user3 = User(
            username="brads213",
            email="brad@gmail.com",
            password=("crazycats2"),
            profile_pic="https://ca.slack-edge.com/T03GU501J-USQFVK3GT-941e867a316f-512",
            bio="I am the father of 2 crazy cats",
    )

    all_users = [user1, user2, user3]
    add_users = [db.session.add(user) for user in all_users]
    db.session.commit()
    return all_users



def undo_users():
    db.session.execute(text("DELETE FROM users"))
    db.session.commit()