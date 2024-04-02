from flask import Flask, render_template, redirect
from .config import Config
from .posts import posts, users
from .forms.post_form import PostForm
from random import randint
from datetime import date

app = Flask(__name__)

app.config.from_object(Config)


# ROUTES
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


@app.route("/new", methods=["GET", "POST"])
def add_post():
    '''Renders the empty post template on GET requests.  
    On POST requests it runs validations and creates a new 
    post resource'''
    form = PostForm()

    if form.validate_on_submit():
        new_post = {
            "id": len(posts) + 1,
            "author": users[randint(0, 2)],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
            "likes": randint(1, 10),
        }
        print(new_post)
        posts.append(new_post)
        return redirect("/all")

    if form.errors:
        print(form.errors)

    return render_template("post_form.html", form=form)
