from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL, Length, Optional


class MovieForm(FlaskForm):
    imageURL = StringField("Image URL", validators=[DataRequired(), URL()])
    genre = StringField("Genre", validators=[DataRequired(), Length(max=255)])
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    imdbrating = DecimalField("IMDb Rating", validators=[DataRequired()])
    released = IntegerField("Released Year", validators=[DataRequired()])
    type = StringField("Type", validators=[DataRequired(), Length(max=255)])
    synopsis = TextAreaField("Synopsis", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
