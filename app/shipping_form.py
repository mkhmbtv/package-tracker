from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

cities = [(city, city) for city in map.keys()]


class ShippingForm(FlaskForm):
    sender = StringField('Sender', [DataRequired()])
    recipient = StringField('Recipient', [DataRequired()])
    origin = SelectField('Origin', [DataRequired()], choices=cities)
    destination = SelectField('Destination', [DataRequired()], choices=cities)
    express_shipping = BooleanField('Express shipping')
    ship = SubmitField('Ship')
    cancel = SubmitField('Cancel')
