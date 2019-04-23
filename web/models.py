from django.db import models

from user.models import User


class Questions(models.Model):
    """
    该模型用于记录面试题的信息
    """
    title = models.CharField(max_length=100, unique=True, null=False, verbose_name='问题题目')
    answer = models.TextField(verbose_name='问题的答案')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 设置当主健用户被删除时，外间问题表中当关联字段设置为null
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='关联用户')
    # 关于面试题设计的技术
    pri_key = models.CharField(max_length=100, null=True, verbose_name='关键字')
    # 出面试题的公司信息
    from_company = models.CharField(max_length=100, null=True, verbose_name='来源')
    is_show = models.IntegerField(default=1, verbose_name='是否公布')
    is_delete = models.IntegerField(default=0, verbose_name='是否删除')
    # 点赞量
    is_like = models.IntegerField(default=0, verbose_name='点赞量')

    class Meta:
        db_table = 'q_questions'


class AgreeQuestions(models.Model):
    """
    该模型用于记录面试题的点赞情况
    """
    ip = models.CharField(max_length=20, null=False, verbose_name='点赞IP地址')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=False, verbose_name='面试题')

    class Meta:
        db_table = 'agree_questions'
