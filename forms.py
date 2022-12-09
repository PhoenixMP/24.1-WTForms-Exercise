"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species = ['Cat', 'Dog', 'Porcupine']


class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name:", validators=[
                       InputRequired('Enter Pet Name')])
    photo_url = StringField("Photo Url:", validators=[
                            Optional(), URL('Enter Valid URL')], )
    species = SelectField('Species', validators=[InputRequired('Choose species')], choices=[
                          (species, species) for species in species])
    age = FloatField("Pet Age:", validators=[
                     Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes:", validators=[Optional()])
    available = BooleanField("Available?")


# class UserForm(FlaskForm):
#     """Form for adding/editing friend."""

#     name = StringField("Name",
#                        validators=[InputRequired()])
#     email = StringField("Email Address",
#                         validators=[Optional(), Email()])
