from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


RATING_CHOICES = ["G", "PG", "R"]


class NewJokeForm(FlaskForm):
    joke = StringField("Joke Body", validators=[DataRequired()])
    punchline = StringField("Punchline", validators=[DataRequired()])
    rating = SelectField('Rating', choices=RATING_CHOICES)
    user = SelectField("Author", choices=[]) 
    submit = SubmitField("Add Joke")
