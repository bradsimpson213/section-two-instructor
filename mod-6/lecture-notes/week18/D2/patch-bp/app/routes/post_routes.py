from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint

posts = Blueprint("posts", __name__)

# print("inside the post BP",__name__)


@posts.route("/all")
def get_all_posts():
    # Query for all posts
    # posts = Post.query.all()
    sorted_posts = sorted(seed_posts, key=lambda post: post['date'], reverse=True)
    return render_template("feed.html", posts=sorted_posts)


@posts.route("/<int:id>")
def get_post_by_id(id):
    print(id)
    # Query
    # post=Post.query.get(id)
    one_post = [post for post in seed_posts if post['id'] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)



@posts.route("/new", methods=['GET', 'POST'])
def create_new_post():
    '''renders an empty form on a get route, validates 
    the form and creates a new post resource on post 
    requests
    '''
    form = PostForm()



    if form.validate_on_submit():
        #enter block and create our resource
        new_post = {
            "id": len(seed_posts) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
            "likes": randint(1, 10)
        }
        print(new_post)
        seed_posts.append(new_post)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    # form.author.choices = #get from the DB
    return render_template("post_form.html", form=form, errors=None)


@posts.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()
   
    if form.validate_on_submit():

        post_to_update = [ post for post in seed_posts if id == post["id"]]

        if post_to_update:
            update_dict = post_to_update[0]
            update_dict["caption"] = form.data["caption"]
            update_dict["author"] = form.data["author"]
            update_dict["image"] = form.data["image"]


        return redirect(f"/posts/{post_to_update['id']}")


    elif form.errors:
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors)

    else:
        current_data =  [ post for post in seed_posts if id == post["id"]]
        print(current_data[0])
        form.process(data=current_data[0])
        return render_template("post_form.html", form=form, type="update", id=id, errors=None)




@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = [post for post in seed_posts if post["id"] == id ]
    if post_to_delete:
        seed_posts.remove(post_to_delete[0])
    return redirect("/posts/all")