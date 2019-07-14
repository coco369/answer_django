from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from user.models import UserLogin


class UserLoginMiddleware(MiddlewareMixin):
    """
        统计用户登陆信息
    """
    def process_response(self, request, response):
        # 执行视图函数之后必执行的中间件方法
        # 需要记录登陆IP，登陆时间，登陆状态
        current_path = request.path
        if current_path == '/api/user/user/login/':

            if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
                login_ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                login_ip = request.META['REMOTE_ADDR']
            # 登陆时间
            login_time = datetime.now()
            # 登陆状态吗
            if eval(response.content.decode('utf-8'))['code'] == 200:
                status = 'SUCCESS'
            else:
                status = 'ERROR'
            # TODO: 后面版本将登陆信息都存储到MONGODB中
            res = {
                'l_ip': login_ip,
                'create_time': login_time,
                'status': status,
            }
            # 保存登陆信息
            UserLogin.objects.create(**res)

        return response
