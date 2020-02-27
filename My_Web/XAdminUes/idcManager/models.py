from django.db import models
from django.contrib.auth.models import User
from system.storage import ImageStorage


# Create your models here.

class IDC(models.Model):
    name = models.CharField(max_length=64, verbose_name= '服务器名称')
    desc = models.CharField(max_length=128, verbose_name= '服务器描述')
    phone = models.CharField(max_length=64, verbose_name= '联系电话')
    address = models.CharField(max_length=128, verbose_name= '所在地')
    create_time = models.DateTimeField(auto_now=True, verbose_name= '录入时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, verbose_name='操作员')

    class Meta:
        verbose_name = 'IDC服务器'
        verbose_name_plural = verbose_name

class ImageDesc(models.Model):
    name = models.CharField(max_length=128, verbose_name= '图片名称')
    image = models.ImageField(upload_to='', storage=ImageStorage())
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, verbose_name='操作员')


    def image_tag(self):
        from XAdminUes.settings import MEDIA_URL
        return '<img height=100px src="%s%s" />' %(MEDIA_URL, self.image)
    
    image_tag.short_description = '图书封面'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = '图片管理'
        verbose_name_plural = verbose_name
