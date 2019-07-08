

from rest_framework import serializers

from user.serializers import UserSerializer
from utils import error
from web.models import Questions


class BackQuestionsSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Questions
        fields = '__all__'


class QuestionsCreateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100, min_length=2, required=True, error_messages={
        'required': '问题标题必填',
        'min_length': '标题不能短于2个字符',
        'max_length': '标题不能长于100个字符',
        'blank': '涉及技术栈必填'
    })
    answer = serializers.CharField(required=True, error_messages={
        'required': '解答必填',
        'blank': '涉及技术栈必填'
    })
    pri_key = serializers.CharField(max_length=100, required=True, error_messages={
        'required': '面试题关键字必填',
        'blank': '涉及技术栈必填'
    })
    from_company = serializers.CharField(max_length=100, required=False, error_messages={
        'max_length': '标题不能长于100个字符'
    })
    is_show = serializers.IntegerField(required=False)

    def validate(self, attrs):
        # 校验保存的面试题是否已存在
        title = attrs.get('title')
        if Questions.objects.filter(title=title).exists():
            raise error.ParamError({'code': 2002, 'msg': '喵了个喵，面试题已存在'})
        return attrs

    def create_questions(self, validate_data, user):
        # 创建面试题方法
        title = validate_data['title']
        answer = validate_data['answer']
        pri_key = validate_data['pri_key']
        # 公司
        from_company = validate_data.get('from_company')
        # is_show字段为非必填值，因此通过get方法获取
        is_show = validate_data.get('is_show', 1)

        # 创建文章
        questions = Questions.objects.create(title=title, answer=answer, pri_key=pri_key,
                                             from_company=from_company, is_show=is_show,
                                             user=user)
        res = {
            'questions': BackQuestionsSerializer(questions).data
        }
        return res


class QuestionsUpdateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100, min_length=2, required=True, error_messages={
        'required': '问题标题必填',
        'min_length': '标题不能短于2个字符',
        'max_length': '标题不能长于100个字符',
        'blank': '涉及技术栈必填'
    })
    answer = serializers.CharField(required=True, error_messages={
        'required': '解答必填',
        'blank': '涉及技术栈必填'
    })
    pri_key = serializers.CharField(max_length=100, required=True, error_messages={
        'required': '面试题关键字必填',
        'blank': '涉及技术栈必填'
    })
    from_company = serializers.CharField(max_length=100, required=False, error_messages={
        'max_length': '标题不能长于100个字符'
    })
    is_show = serializers.IntegerField(required=False)

    def update_questions(self, validate_data, instance):
        # 修改面试题方法
        instance.title = validate_data['title']
        instance.answer = validate_data['answer']
        instance.pri_key = validate_data['pri_key']
        instance.from_company = validate_data.get('from_company')
        # is_show字段为非必填值，因此通过get方法获取
        instance.is_show = validate_data.get('is_show', 1)
        instance.save()
        res = {
            'questions': BackQuestionsSerializer(instance).data
        }
        return res
