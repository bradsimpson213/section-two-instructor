from flask import Blueprint, render_template, redirect, request
# from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, User, Post
from .AWS_helpers import upload_file_to_AWS, get_unique_filename, remove_file_from_AWS


posts = Blueprint("posts", __name__)

# print("inside posts BP", __name__)


@posts.route("/all")
def get_all_posts():
    """get all posts and display them"""
    posts = Post.query.order_by(Post.post_date.desc()).all()
    print(posts)
    # sorted_posts = sorted(seed_posts, key=lambda post: post['date'], reverse=True)
    # return render_template("feed.html", posts=posts)
    response = [post.to_dict() for post in posts]
    print(response)
    return {"posts": response }



@posts.route("/<int:id>")
def get_post_by_id(id): 
    """return a single post by its ID"""
    print(id)
    one_post = Post.query.get(id)
    # print(one_post.to_dict(user=True))
    return render_template("feed.html", posts=[one_post])

       

@posts.route("/new", methods=["GET", "POST"])
def add_new_post():
    """returns a new post form on get requests, 
    validates and saves the new resource on post"""

    form = PostForm()
    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    # print(form.author.choices)
    # query for data if needed in the form
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        # print(selected_user)

        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_AWS(image)

        if "url" not in upload:
            return render_template("post_form.html", form=form, type="post", errors=[upload])

        new_post =Post(
            user=selected_user,
            caption= form.data["caption"],
            image= upload["url"],
            post_date= date.today(),
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
   
        # return redirect("/posts/all")
        return {"resPost": new_post.to_dict()}

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, type="post", errors=form.errors)


    return render_template("post_form.html", form=form, type="post", errors=None)



@posts.route("/update/<int:id>", methods=["GET", "POST"])
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



@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)

    file_delete = remove_file_from_AWS(post_to_delete.image)

    if file_delete: 
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/posts/all")

    else:
        return "<h1>File delete error!</h1>"