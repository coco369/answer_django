import re
from datetime import datetime, timedelta

from django.utils.deprecation import MiddlewareMixin

from user.models import Visit


class UserVisitMiddleware(MiddlewareMixin):
    """
        访问量统计
    """
    def process_request(self, request):
        # 统计访问接口的用户量，如果同一个IP在一分钟内多次访问网站，则算一次访问

        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        # 记录用户访问的面试题id值，并存储 /api/web/questions/[id]/
        if re.match('/api/web/questions/(\d+)/', request.path):
            # 如果用户访问面试题详情，则判断访问记录，并做记录
            patterns = re.compile('/api/web/questions/(\d+)/')
            result = patterns.findall(request.path)[0] if patterns.findall(request.path) else None
            visit = Visit.objects.filter(v_ip=ip, q_id=result).first()
            if visit:
                if datetime.utcnow() < visit.create_time.replace(tzinfo=None) + timedelta(minutes=1):
                    return None
            else:
                Visit.objects.create(v_ip=ip, q_id=result)
        else:
            # 如果用户访问非面试题详情页面，则只记录访问的ip地址
            visit = Visit.objects.filter(v_ip=ip).order_by('-id').first()
            if visit:
                if datetime.utcnow() < visit.create_time.replace(tzinfo=None) + timedelta(minutes=1):
                    return None
            else:
                Visit.objects.create(v_ip=ip)
