from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL, Length, Email 


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    submit = SubmitField("Login")   



class SignUpForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(), Length(min=4)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    profile_pic = StringField("Profile Pic URL", validators=[DataRequired(), URL()])
    bio = StringField("Bio")
    submit = SubmitField("Create User")



class LogoutForm(FlaskForm):
    submit = SubmitField("Logout")