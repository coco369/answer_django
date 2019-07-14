from django.utils.deprecation import MiddlewareMixin


class UserVisitMiddleware(MiddlewareMixin):
    """
        访问量统计
    """
    def process_request(self, request):
        # 统计访问接口的用户量，如果同一个IP在一分钟内多次访问网站，则算一次访问

        return None
