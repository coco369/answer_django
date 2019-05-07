
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from back.authentications import AuthAuthenticateClass
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


