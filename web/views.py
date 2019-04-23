from django.db.models import Q
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from utils import error
from web.models import Questions, AgreeQuestions
from web.serializers import QuestionsSerializer


class QuestionsView(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):

    queryset = Questions.objects.filter(is_delete=0).all()
    serializer_class = QuestionsSerializer

    @list_route(['GET'])
    def ranking(self, request, *args, **kwargs):
        # 查询排名前十的内容,通过过滤点赞量进行排序
        queryset = self.get_queryset().order_by('-is_like', '-id')[:10]
        serializers = QuestionsSerializer(queryset, many=True)
        return Response(serializers.data)

    @list_route(['GET'])
    def new(self, request, *args, **kwargs):
        # 查询最新的前十道面试题内容
        queryset = self.get_queryset().order_by('-id')[:10]
        serializers = QuestionsSerializer(queryset, many=True)
        return Response(serializers.data)

    @detail_route(['POST'])
    def agree(self, request, pk=None):
        # 定义detail_route后，接口地址为：/api/web/questions/[id]/agree/
        # 逻辑: 点赞时将记录用户的ip地址，一个ip地址只能对应一个面试题进行点赞
        ip = self.request.META.get('REMOTE_ADDR')
        if AgreeQuestions.objects.filter(ip=ip, question_id=pk).exists():
            raise error.ParamError({'code': 2003, 'msg': '喵了个喵，您已对该面试题点过赞啦，不用再点人家啦'})
        AgreeQuestions.objects.create(ip=ip, question_id=pk)
        # 修改点赞数(自增1)
        question = Questions.objects.filter(id=pk).first()
        question.is_like += 1
        question.save()

        res = {
            'is_like': question.is_like
        }
        return Response(res)

    @list_route(['GET'])
    def search(self, request, *args, **kwargs):
        # 搜索面试题功能
        # 搜索内容包括面试题目，公司，技术，面试解答
        wd = self.request.query_params.get('wd')
        queryset = self.get_queryset().filter(Q(title__contains=wd) |
                                              Q(from_company__contains=wd) |
                                              Q(pri_key__contains=wd) |
                                              Q(answer__contains=wd)).all()
        serializers = QuestionsSerializer(queryset, many=True)
        return Response(serializers.data)



