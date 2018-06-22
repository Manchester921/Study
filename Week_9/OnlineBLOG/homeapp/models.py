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

    def __unicode__(self):
        return self.acId
    pass


class BlogInfo(models.Model):
    blogId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    publishTime = models.DateTimeField(auto_now_add = True)
    content = models.TextField(null=True)
    acId = models.ForeignKey(BlogAcc, on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.blogId
    pass
    

class BlogCategory(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)
    blogId = models.ForeignKey(BlogInfo, on_delete=models.CASCADE,)
    
class BlogComment(models.Model):
    comId = models.AutoField(primary_key=True)
    comTime = models.DateTimeField(auto_now_add = True)
    comContent = models.TextField(null=True)
    acId = models.ForeignKey(BlogAcc, on_delete=models.CASCADE,)

    