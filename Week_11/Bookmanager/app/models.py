from django.db import models
from django.contrib.auth.models import User
from system.storage import ImageStorage
# Create your models here.

class BookCategory(models.Model):

    name = models.CharField(max_length=64, verbose_name= '图书名称')
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, verbose_name='操作员')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '图书类别'
        verbose_name_plural = verbose_name

class Book(models.Model):
    bname = models.CharField(max_length=64, verbose_name= '图书名称')
    image = models.ImageField(upload_to='', storage=ImageStorage())
    publish = models.CharField(max_length=64, verbose_name= '出版社')
    author = models.CharField(max_length=64, verbose_name= '作者')
    bookcategory = models.ForeignKey(BookCategory, on_delete=models.CASCADE,verbose_name='图书馆类别')
    create_time = models.DateTimeField(auto_now=True, verbose_name= '录入时间')

    class Meta:
        verbose_name = '图书管理'
        verbose_name_plural = verbose_name
    
    def image_tag(self):
        from Bookmanager.settings import MEDIA_URL
        return '<img height=100px src="%s%s" />' %(MEDIA_URL, self.image)
    
    image_tag.short_description = '图书封面'
    image_tag.allow_tags = True


