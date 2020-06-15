from flask_wtf import FlaskForm
from wtforms import StringField, RadioField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,Length, ValidationError


class ItemForm(FlaskForm):
    hyip = StringField("Input HYIP Item", validators=[DataRequired(), Length(min=5, max=10)])

    status_select = RadioField("Status", choices=[('pending','Pending'),('paying','Paying'),('notpaying','Not Paying')], validate_choice=True)
    status_select.default = 'pending'

    description = TextAreaField("Item Description", validators=[DataRequired()])

    submit = SubmitField("Post Item!")