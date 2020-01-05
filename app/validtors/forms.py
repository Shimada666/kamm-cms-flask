from flask_wtf import FlaskForm
from flask import request, flash
from app.exceptions.base import ParameterException
from app.libs.utils import common_render
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField, IntegerField, \
    FieldList
from wtforms.validators import DataRequired, Email, length, Optional, URL, EqualTo, Regexp, NumberRange
from app.models.user import Group
from app.exceptions.base import WebNotFound


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


# 注册校验
class RegisterForm(Form):
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码长度必须在6~22位之间，包含字符、数字和 _ '),
        EqualTo('confirm_password', message='两次输入的密码不一致，请输入相同的密码')])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(message='请确认密码')])
    username = StringField(validators=[DataRequired(message='用户名不可为空'),
                                       length(min=2, max=10, message='用户名长度必须在2~10之间')])

    # group_id = IntegerField('分组id',
    #                         validators=[DataRequired(message='请输入分组id'), NumberRange(message='分组id必须大于0', min=1)])
    email = StringField('电子邮箱', validators=[
        Regexp(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', message='电子邮箱不符合规范，请输入正确的邮箱'),
        Optional()
    ])
    submit = SubmitField()

    # def validate_group_id(self, value):
    #     exists = Group.query.filter_by(id=value).first()
    #     if not exists:
    #         raise WebNotFound(msg='分组不存在')


# 管理员创建分组
class NewGroup(Form):
    # 分组name
    name = StringField(validators=[DataRequired(message='请输入分组名称')])
    # 非必须
    info = StringField(validators=[Optional()])
    # 必填，分组的权限
    auths = FieldList(StringField(validators=[DataRequired(message='未勾选权限')]),
                      validators=[DataRequired(message='请输入auths字段')])
    submit = SubmitField()


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
