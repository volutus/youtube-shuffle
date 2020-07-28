from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RandomizerForm(FlaskForm):
    playlist_id = StringField('Playlist ID', validators=[DataRequired()])
    submit = SubmitField("Randomize!")
