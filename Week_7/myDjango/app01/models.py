from django.db import models

# Create your models here.

class BookCategory(models.Model):
    bcid = models.AutoField(primary_key=True)
    bcname = models.CharField(max_length=30)
    pass

class DepInfo(models.Model):
    depId = models.AutoField(primary_key=True)
    depName = models.CharField(max_length=30)
    depLoc = models.CharField(max_length=30)
    pass



# from app01.models import BookCategory
# obj = BookCategory(bcname = 'Python Book')
# obj.save()

# BookCategory.objects.Create(bcname = 'Java Book')



