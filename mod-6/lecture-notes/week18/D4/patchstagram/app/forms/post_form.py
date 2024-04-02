from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL



class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5, message="Posts catpion must be at least 5 characters")])
    image_url = StringField("Image URL", validators=[DataRequired(), URL()])
    author = SelectField("Author", choices=[])
    submit = SubmitField("Create Post")


