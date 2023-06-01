from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField("Titulo", validators=[DataRequired()])
    subtitle = StringField("Subtitulo", validators=[DataRequired()])
    img_url = StringField("URL de imagem", validators=[DataRequired(), URL()])
    body = CKEditorField("Conteúdo", validators=[DataRequired()])
    submit = SubmitField("Enviar")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    name = StringField("Nome", validators=[DataRequired()])
    submit = SubmitField("Inscrever-me!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Deixe me entrar!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comentar", validators=[DataRequired()])
    submit = SubmitField("Enviar comentário")
