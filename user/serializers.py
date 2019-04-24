
import uuid

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from django.core.cache import cache

from user.models import User
from utils import error


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'is_delete']


class LoginSerializer(serializers.Serializer):
    # 登录序列化
    username = serializers.CharField(max_length=4, min_length=2, required=True, error_messages={
        'required': '账号必填',
        'max_length': '用户名不能超过4字符',
        'min_length': '用户名不能短于2字符'
    })
    password = serializers.CharField(min_length=6, max_length=20, error_messages={
        'required': '密码必填',
        'max_length': '密码不能超过20字符',
        'min_length': '密码不能短于6字符'
    })

    def validate(self, attrs):
        # 校验参数的方法，validate
        username = attrs.get('username')
        password = attrs.get('password')
        # 判断账号是否已经注册，如果没有注册，则抛出错误
        if not User.objects.filter(username=username).exists():
            raise error.ParamError({'code': 1001, 'msg': '登录账号不存在，请更换账号再登录'})
        # 判断账号和密码是否正确
        user = User.objects.filter(username=username).first()
        if not check_password(password, user.password):
            raise error.ParamError({'code': 1002, 'msg': '账号或密码错误，请确认登录信息'})
        return attrs

    def login_data(self, validate_data):
        # 实现登录功能
        user = User.objects.filter(username=validate_data['username']).first()
        token = uuid.uuid4().hex
        # 使用缓存cache
        cache.set(token, user.id, timeout=60 * 60 * 7 * 24)

        res_data = {
            'msg': '请求成功',
            'user_id': user.id,
            'username': user.username,
            'token': token
        }
        return res_data


class RegisterSerializer(serializers.Serializer):
    # 登录序列化
    username = serializers.CharField(required=True, max_length=4, min_length=2, error_messages={
        'required': '用户名必填',
        'max_length': '用户名不能超过4字符',
        'min_length': '用户名不能短于2字符'
    })
    password = serializers.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '密码必填',
        'max_length': '密码不能超过20字符',
        'min_length': '密码不能短于6字符'
    })
    password2 = serializers.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '确认密码必填',
        'max_length': '密码不能超过20字符',
        'min_length': '密码不能短于6字符'
    })

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        # 判断如果账号已存在则抛出错误提示
        if User.objects.filter(username=username).exists():
            raise error.ParamError({'code': 1003, 'msg': '注册账号已存在，请更换账号'})
        # 判断密码和确认密码是否一致
        if password != password2:
            raise error.ParamError({'code': 1004, 'msg': '注册密码和确认密码不一致'})
        # 返回校验的参数
        return attrs

    def register_data(self, validate_data):
        # 注册操作
        u_password = make_password(validate_data['password'])
        user = User.objects.create(username=validate_data['username'],
                                   password=u_password)
        res_data = {
            'msg': '请求成功',
            'user_id': user.id
        }
        return res_data
