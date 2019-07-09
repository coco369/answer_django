
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, LoginSerializer, RegisterSerializer, ResetPasswordSerializer
from utils import error


class UserView(viewsets.GenericViewSet,
               mixins.ListModelMixin):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['POST'], serializer_class=LoginSerializer)
    def login(self, request):
        # 登录操作
        # 将请求的参数进行序列化，并且做校验
        serializer = self.serializer_class(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if not result:
            errors = serializer.errors
            data = {'code': 1002, 'msg': '账号或密码错误，请确认登录信息'}
            data['error'] = errors
            raise error.ParamError(data)
        # 实现注册
        data = serializer.login_data(serializer.data)
        return Response(data)

    @list_route(methods=['POST'], serializer_class=RegisterSerializer)
    def register(self, request):
        """
        注册操作
        """
        # 将请求的参数进行序列化，并且做校验
        serializer = self.serializer_class(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if not result:
            errors = serializer.errors
            data = {'code': 1002, 'msg': '账号或密码错误，请确认登录信息'}
            data['error'] = errors
            raise error.ParamError(data)
        # 实现注册
        data = serializer.register_data(serializer.data)
        return Response(data)

    @list_route(methods=['POST'], serializer_class=ResetPasswordSerializer)
    def reset_password(self, request):
        """
        重置密码
        """
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if not result:
            errors = serializer.errors
            data = {'code': 1007, 'msg': '重置密码不成功', 'error': errors}
            raise error.ParamError(data)
        # 实现重置
        serializer.reset(serializer.data)
        res = {
            'msg': '重置密码成功'
        }
        return Response(res)
