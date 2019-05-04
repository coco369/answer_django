import logging
import time

try:
    # needed to support Django >= 1.10 MIDDLEWARE
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # needed to keep Django <= 1.9 MIDDLEWARE_CLASSES
    MiddlewareMixin = object

# 获取logger
logger = logging.getLogger(__name__)


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # url到服务器的时候，经过中间件最先执行的方法
        request.init_time = time.time()
        request.init_body = request.body

    def process_response(self, request, response):
        try:
            # 经过中间件，最后执行的方法
            # 计算请求到响应的时间
            count_time = time.time() - request.init_time
            # 获取响应的状态码
            code = response.status_code
            # 获取请求的内容
            req_body = request.init_body
            # 获取想要的内容
            res_body = response.content

            msg = '%s %s %s %s' % (count_time, code, req_body, res_body)
            # 写入日志信息
            logger.info(msg)
        except Exception as e:
            logger.critical('log error, Exception:%s' % e)

        return response
