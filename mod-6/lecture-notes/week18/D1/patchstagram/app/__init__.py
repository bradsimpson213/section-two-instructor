from flask import Flask, render_template
from .config import Config
from .posts import posts

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def index():
    '''renders the home page'''
    return render_template("index.html")


@app.route('/all')
def get_all_posts():
    '''get all posts route, will build your feed in 
    descdenting order based on post date'''
    # Query for all posts
    # all_posts = Posts.query.all()
    sorted_posts = sorted(posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=sorted_posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    '''returns a single post by id when supplied with 
    an id as a route parameter'''
    one_post = [post for post in posts if post['id'] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)