from rest_framework.exceptions import APIException


class ParamError(APIException):
    """ http参数错误
    """

    def __init__(self, err):
        self.detail = err

    def __str__(self):
        return self.msg
