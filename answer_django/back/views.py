from datetime import datetime, timedelta

from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route, api_view, authentication_classes
from rest_framework.response import Response

from user.models import Visit
from utils.authentications import AuthAuthenticateClass
from utils import error
from web.models import Questions
from back.serializers import BackQuestionsSerializer, QuestionsCreateSerializer, QuestionsUpdateSerializer


class QuestionsView(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = Questions.objects.filter(is_delete=0).all()
    serializer_class = BackQuestionsSerializer
    authentication_classes = (AuthAuthenticateClass,)

    def create(self, request, *args, **kwargs):
        # 创建面试题
        serializers = QuestionsCreateSerializer(data=request.data)
        result = serializers.is_valid(raise_exception=False)
        if not result:
            raise error.ParamError({'code': 2001, 'msg': '面试题字段校验有误', 'error': serializers.errors})
        data = serializers.create_questions(serializers.data, request.user)
        return Response(data)

    def perform_destroy(self, instance):
        # 实现软删除面试题
        instance.is_delete = 1
        instance.save()
        serializers = BackQuestionsSerializer(instance)
        return Response(serializers.data)

    def update(self, request, *args, **kwargs):
        # 获取修改面试题对象
        instance = self.get_object()
        # 校验和序列化
        serializers = QuestionsUpdateSerializer(data=request.data)
        result = serializers.is_valid(raise_exception=False)
        if not result:
            raise error.ParamError({'code': 2001, 'msg': '面试题字段校验有误', 'error': serializers.errors})
        data = serializers.update_questions(serializers.data, instance)
        return Response(data)

    @list_route(methods=['GET'])
    def count(self, request):
        """
        统计当前发布的面试题的数量
        """
        q_counts = self.queryset.count()
        res = {
            'count': q_counts
        }
        return Response(res)


@api_view()
@authentication_classes((AuthAuthenticateClass,))
def user_visit(request):
    """
        今日用户访问量
    """
    now_time = datetime.now().strftime('%Y-%m-%d 00:00:00')
    tomorrow_time = datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S') - timedelta(hours=8)
    today_time = datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=16)
    today_visit = Visit.objects.filter(create_time__gt=tomorrow_time, create_time__lt=today_time).count()
    res = {
        'today_visit':today_visit
    }
    return Response(res)
