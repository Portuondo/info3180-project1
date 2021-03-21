from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length

class PropertyForm(FlaskForm):


    title = StringField('Property Title' , validators=[DataRequired()]),
    description = StringField('Description', validators=[DataRequired()]),
    no_of_bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired()]),
    no_of_bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()]),
    price= IntegerField('Price', validators=[DataRequired()]),
    typep= SelectField('propertyType', validators=[DataRequired()]),
    location=StringField('Location', validators=[DataRequired()]),
    photolocation= FileField('propertyImage', validators=[DataRequired()]),




    