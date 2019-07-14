
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from user.models import User
from utils import error


class AuthAuthenticateClass(BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.query_params.get('token') if request.query_params.get('token') else request.data.get('token')
            # 从缓存中校验用户的信息
            user_id = cache.get(token)
            if not user_id:
                raise error.ParamError({'code': 1005, 'msg': '登陆状态已失效，请重新登陆'})
            # 获取用户对象
            user = User.objects.get(pk=user_id)
            return user, token
        except Exception as e:
            raise error.ParamError({'code': 1006, 'msg': '用户认证失败，请重新登陆'})
