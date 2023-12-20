from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL, Length, Optional, NumberRange, EqualTo

class MovieForm(FlaskForm):
    imageURL = StringField("Image URL", validators=[DataRequired(), URL(message="Invalid URL format")])
    genre = StringField("Genre", validators=[DataRequired(), Length(max=10), EqualTo('horror', message="Genre must be 'horror'")])
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    imdbrating = DecimalField("IMDb Rating", validators=[DataRequired(), NumberRange(min=0, max=10, message="Rating must be between 0 and 10")])
    released = IntegerField("Released Year", validators=[DataRequired(), NumberRange(min=1800, max=2100, message="Enter a valid release year")])
    type = StringField("Type", validators=[DataRequired(), Length(max=20)])
    synopsis = TextAreaField("Synopsis", validators=[DataRequired(), Length(max=1000, message="Synopsis must be 1000 characters or less")])
    submit = SubmitField("Add Movie")


