from flask import Flask, render_template, redirect
from .config import Config
from .posts import posts, users
from .forms.post_form import PostForm
from random import randint
from datetime import date
from .models import db, Post, User

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

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
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    # sorted_posts = sorted(posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=all_posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    '''returns a single post by id when supplied with 
    an id as a route parameter'''
    # one_post = [post for post in posts if post['id'] == id]
    one_post = Post.query.get(id)
    print(one_post)
    return render_template("feed.html", posts=[one_post])


@app.route("/new", methods=["GET", "POST"])
def add_post():
    '''Renders the empty post template on GET requests.  
    On POST requests it runs validations and creates a new 
    post resource'''
    form = PostForm()

    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    print(form.author.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data['author'])
        print(selected_user)

        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image_url"],
            post_date=date.today(),
            user=selected_user,
        )
        
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)


    return render_template("post_form.html", form=form, errors=None)







@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()

    form.author.choices = [ (user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        post_to_update = Post.query.get(id)

        selected_user = User.query.get(form.data["author"])
        post_to_update.user = selected_user
        post_to_update.caption = form.data["caption"]
        post_to_update.image = form.data["image"]
        db.session.commit()
        return redirect(f"/posts/{post_to_update.id}")


    elif form.errors:
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, type="update", id=id, errors=None)



@app.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")