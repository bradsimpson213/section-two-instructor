from dad_jokes.models.db import db, User, Joke
from dad_jokes import app


with app.app_context():
    
    db.drop_all()
    print("All table dropped!")
    db.create_all()
    print("Create all tables!")

    user1 = User(username="Brad", email="brad@gmail.com", password="password")
    user2 = User(username="Andy", email="andy@gmail.com", password="cubingiscool")
    user3 = User(username="Blue", email="blue@gmail.com", password="iamaninja")
    user4 = User(username="Patch", email="patch@gmail.com", password="ilovefud")


    joke1 = Joke(
        joke_body='What did the plumber say to the singer?',
        punchline='Nice pipes...',
        rating='G',
        user=user1,
        joke_likes=[user2, user3]
    )

    joke2 = Joke(
        joke_body='What do you call a lazy doctor?',
        punchline='Dr Doo-little...',
        rating='PG',
        user=user1,
        joke_likes=[user1, user2, user4]
    )

    joke3 = Joke(
        joke_body='What do you call a camel in a drought?',
        punchline='A dry humper...',
        rating='PG',
        user=user1
    )

    joke4 = Joke(
        joke_body='Did you hear Steve Harvey and his wife got into a fight?',
        punchline='It was a real family feud...',
        rating='R',
        user=user2,
        joke_likes=[user3, user4]
    )

    joke5 = Joke(
        joke_body='What do mermaids wash their fins with?',
        punchline='Tide...',
        rating='G',
        user=user2,
        joke_likes=[user1, user3, user4]
    )

 

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(joke1)
    db.session.add(joke2)
    db.session.add(joke3)
    db.session.add(joke4)
    db.session.add(joke5)
    db.session.commit()
    print("DB was seeded!")