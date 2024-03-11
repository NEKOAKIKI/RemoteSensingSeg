from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    """
    用户表
    """
    nid = models.AutoField(primary_key=True)
    tel = models.CharField(verbose_name='手机号', max_length=12, null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name='ip地址', default='117.132.46.143')
    addr = models.CharField(max_length=128, verbose_name='用户地址信息', null=True, blank=True)
    name = models.CharField(max_length=238, verbose_name='姓名', null=True, blank=True)
    sex = models.CharField(max_length=128, verbose_name='性别', null=True, blank=True)
    age = models.CharField(max_length=128, verbose_name='年龄', null=True, blank=True)
    role = models.CharField(max_length=128, verbose_name='用户角色', default='普通用户')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户管理'


class Avatars(models.Model):
    """
    图片表
    """
    nid = models.AutoField(primary_key=True)
    url = models.FileField(verbose_name='图片地址', upload_to='avatars/')

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name_plural = ' 图片管理'


class Record(models.Model):
    """
    历史记录表
    """
    nid = models.AutoField(primary_key=True)
    avatars = models.ForeignKey(
        to='Avatars',
        to_field='nid',
        on_delete=models.SET_NULL,
        verbose_name='上传图片', null=True, blank=True
    )

    user = models.ForeignKey(
        to='UserInfo',
        to_field='nid',
        on_delete=models.SET_NULL,
        verbose_name='上传用户', null=True, blank=True
    )

    result_url = models.CharField(verbose_name='分割结果', max_length=256, null=True)

    create_date = models.DateTimeField(verbose_name='日期', auto_now_add=True, null=True)


    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name_plural = '历史记录'


