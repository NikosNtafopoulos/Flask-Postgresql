'''FlaskForms[flask_wtf] allow us to present our form with python classes'''
#EqualTo() to set what you want to compare
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from app.models import UserInfo

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
    # custom validation
    '''def validate_field(self,field):
        if True:
            raise ValidationError('Validation Message')
    '''
    #check if user exists in our database by email
    def validate_email(self,email):
        email = UserInfo.query.filter_by(email=email.data).first()
        # if user exists throw a validation error
        if email:
            raise ValidationError('That email belongs to another user')

    # check if user exists in our database by email
    def validate_lastName(self, last_name):
        last_name = UserInfo.query.filter_by(last_name=last_name.data).first()
        if last_name:
            raise ValidationError('That email belongs to another user')


# form class for login WITH EMAIL and PASSWORD after registration
class ClientLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Pass', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')