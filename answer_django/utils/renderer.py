from rest_framework.renderers import JSONRenderer


class CustomJsonRender(JSONRenderer):
    """ 自定义返回数据 Json格式
    {
        "code": 0,
        "msg": "success",
        "data": { ... }
    }
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            msg = data.pop('msg')
            code = data.pop('code')
        except:
            msg = '请求成功'
            code = 200

        response = renderer_context['response']
        response.status_code = 200

        res = {
            'code': code,
            'msg': msg,
            'data': data,
        }
        print(res)
        return super().render(res, accepted_media_type, renderer_context)
