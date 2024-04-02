from flask import Blueprint, redirect, render_template, flash
# from ..posts import posts as file_posts
from ..forms import PostForm, LogoutForm
from datetime import date
from random import randint
from ..models import db, Post, User
from flask_login import current_user, login_required


posts = Blueprint("posts", __name__)


@posts.route("/all")
@login_required
def get_all_posts():
    """route to fetch and display all posts"""
    # Query our DB to get all posts
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    print(all_posts)
    logout_form = LogoutForm()
    # all_posts_dict = [post.to_dict() for post in all_posts]
    # print(all_posts_dict)
    return render_template("feed.html", posts=all_posts, logout_form=logout_form, user=current_user )
    # return {"response": all_posts_dict}



@posts.route("/<int:id>")
@login_required
def get_post_by_id(id):
    """returns a single post by the given route param id"""
    one_post = Post.query.get(id)
    print(one_post.to_dict())
    logout_form = LogoutForm()
    # one_post = [post for post in file_posts if post["id"] == id ]
    return render_template("feed.html", posts=[one_post], user=current_user, logout_form=logout_form)
    # return one_post.to_dict()



@posts.route("/new", methods=["GET", "POST"])
@login_required
def create_post():
    """handles displaying a new post form on get requests 
    and validating submitted data on post requests"""
    form = PostForm()
    logout_form = LogoutForm()

    if form.validate_on_submit():  

        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image"],
            post_date = date.today(),
            user=current_user
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")


    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, type="post", errors=form.errors, user=current_user, logout_form=logout_form)

    return render_template("post_form.html", form=form, type="post", errors=None, user=current_user, logout_form=logout_form)



@posts.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update_post(id):
    form = PostForm()
    logout_form = LogoutForm()

    if form.validate_on_submit():
        post_to_update = Post.query.get(id)
    
        post_to_update.caption = form.data["caption"]
        post_to_update.image = form.data["image"]
        post_to_update.post_date = date.today()

        db.session.commit()
        return redirect(f"/posts/{post_to_update.id}")

    elif form.errors:
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors, user=current_user, logout_form=logout_form)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, type="update", id=id, errors=None, user=current_user, logout_form=logout_form)



@posts.route("/delete/<int:id>")
@login_required
def delete_post(id):
    post_to_delete = Post.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")





@posts.route("/like/<int:id>")
def like_post(id):
    like_post = Post.query.get(id)
    if current_user not in like_post.post_likes:
        like_post.post_likes.append(current_user)
        db.session.commit()
        flash("You just liked this post! 😁", id)
    else:
        flash("You can't like a post you already liked!", id)

    return redirect("/posts/all")


@posts.route("/dislike/<int:id>")
def unlike_post(id):
    like_post = Post.query.get(id)
    if current_user in like_post.post_likes:
        like_post.post_likes.remove(current_user)
        db.session.commit()
        flash("You just disliked this post! 🙁", id)
    else:
        flash("You can't dislike a post you never liked!", id)

    return redirect("/posts/all")