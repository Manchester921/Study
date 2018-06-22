from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class BlogAcc(models.Model):
    acId = models.AutoField(primary_key=True)
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    registerTime = models.DateTimeField(auto_now_add = True)
    mark = models.TextField(null=True)
    accPic = models.ImageField(upload_to='accPic', null=True)
    # gender = models.BooleanField(null=True)
    birthday = models.DateTimeField(null=True)

    pass
