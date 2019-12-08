from flask_wtf import FlaskForm
from flask import request, flash
from app.exceptions.base import ParameterException, FormErrorException
from app.libs.utils import common_render
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, length, Optional, URL, EqualTo, Regexp


class Form(FlaskForm):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(Form, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(Form, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    @property
    def errors_info(self):
        errors_lst = []
        for k, v in self.errors.items():
            errors_lst += v
        errors_str = '<br>'.join(errors_lst)
        return errors_str


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class ResetPasswordForm(Form):
    oldPassword = PasswordField('oldPassword', validators=[DataRequired()])
    newPassword = PasswordField('newPassword', validators=[DataRequired()])
    newPassword2 = PasswordField('newPassword2',
                                 validators=[DataRequired(), EqualTo('newPassword', message='两次输入密码不同！')])
    submit = SubmitField('submit')


class UserInfoForm(Form):
    real_name = StringField('real_name')
    gender = StringField('gender')
    phone = StringField('phone')
    birthday = StringField('birthday')
    email = StringField('email', validators=[
        Regexp(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', message='电子邮箱不符合规范，请输入正确的邮箱'),
        Optional()
    ])
    about = StringField('about')
    submit = SubmitField('submit')


class AddLinkForm(Form):
    title = StringField('title')
    url = StringField('url')
    email = StringField('email')
    create_time = StringField('create-time')
    submit = SubmitField('submit')
