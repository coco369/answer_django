from django.db import models


class User(models.Model):
    """
        用户模型
    """
    username = models.CharField(null=False, max_length=4, verbose_name='用户名称')
    password = models.CharField(max_length=255, null=False, verbose_name='密码')
    # 用户创建时，默认创建时间字段
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 用户被删除状态字段，默认为0。0表示账号可用，1表示账号已删除，不可用
    is_delete = models.BooleanField(default=0, verbose_name='是否被删除')

    class Meta:
        db_table = 'q_user'


class Visit(models.Model):
    """
        用户访问量模型
    """
    v_ip = models.CharField(max_length=30, null=False, verbose_name='访问用户的IP地址')
    q_id = models.IntegerField(null=True, verbose_name='用户访问的面试题id值')
    # 访问记录被创建时，默认创建时间字段
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'q_visit'


class UserLogin(models.Model):
    """
        用户登陆信息记录模型
    """
    STATUS = (
        ('SUCCESS', '成功'),
        ('ERROR', '失败')
    )
    l_ip = models.CharField(max_length=30, null=False, verbose_name='登陆IP地址')
    status = models.CharField(max_length=10, choices=STATUS, default='SUCCESS')
    # 访问记录被创建时，默认创建时间字段
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'q_user_login'
