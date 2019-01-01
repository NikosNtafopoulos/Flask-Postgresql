'''FlaskForms[flask_wtf] allow us to present our form with python classes'''
#EqualTo() to set what you want to compare
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# form class for registration
class ClientForm(FlaskForm):
    first_name = StringField('Firstname',
                             validators=[DataRequired(),
                                         Length(min=2, max=20)])
    last_name = StringField('Lastname', validators=[DataRequired(), Length(min=4,max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')


# form class for login WITH EMAIL and PASSWORD after registration
class ClientLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Pass', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')