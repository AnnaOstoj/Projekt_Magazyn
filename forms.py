from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError



class ProductForm(FlaskForm):
    name = StringField('Product Name', [DataRequired()])
    unit = StringField('Unit', [DataRequired()])
    unit_price = IntegerField('Unit Price', [DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])

class ProductSaleForm(FlaskForm):
    sold_quantity = IntegerField('Sold Quantity', [DataRequired()])