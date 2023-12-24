from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL, Length, Optional, NumberRange, EqualTo,ValidationError
# Custom validator for genre
def validate_genre(form, field):
    if field.data != "horror":
        raise ValidationError("Genre must be 'horror'")

class MovieForm(FlaskForm):
    imageURL = StringField("Image URL", validators=[DataRequired(), URL(message="Invalid URL format")])
    genre = StringField("Genre", validators=[DataRequired(), Length(max=10), validate_genre])
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    imdbrating = DecimalField("IMDb Rating", validators=[DataRequired()])
    released = IntegerField("Released Year", validators=[DataRequired(), NumberRange(min=1800, max=2100, message="Enter a valid release year")])
    type = StringField("Type", validators=[DataRequired(), Length(max=20)])
    synopsis = TextAreaField("Synopsis", validators=[DataRequired(), Length(max=1000, message="Synopsis must be 1000 characters or less")])
    submit = SubmitField("Add Movie")


