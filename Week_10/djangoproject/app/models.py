from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # 确定该模型与框架内置User模型的关系（一对一）
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    # 在User模型基础上需要扩展的属性
    phone = models.CharField(max_length=30)
    pass