# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, CreatePostForm, CommentForm
from datetime import date
from models import User, BlogPost, Comment, db
from functools import wraps

routes = Blueprint('routes', __name__)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function


@routes.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            User.query.filter_by(email=form.email.data).first()
            flash("Este email já foi cadastrado anteriormente, entre ao inves de cadastrar!")
            return redirect(url_for('routes.login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("routes.get_all_posts"))

    return render_template("register.html", form=form, current_user=current_user)


@routes.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Este email nao possui conta! Por favor, tente novamente.")
            return redirect(url_for('routes.login'))
        elif not check_password_hash(user.password, password):
            flash('Senha incorreta! Por favor, tente novamente.')
            return redirect(url_for('routes.login'))
        else:
            login_user(user)
            return redirect(url_for('routes.get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user)


@routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.get_all_posts'))


@routes.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Voce precisa cadastrar ou entrar para comentar.")
            return redirect(url_for("routes.login"))

        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", post=requested_post, form=form, current_user=current_user)


@routes.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@routes.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


@routes.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("routes.get_all_posts"))

    return render_template("make-post.html", form=form, current_user=current_user)


@routes.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=current_user,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("routes.show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@routes.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('routes.get_all_posts'))
