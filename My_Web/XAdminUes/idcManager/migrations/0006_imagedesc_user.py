# Generated by Django 2.0.5 on 2018-06-20 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idcManager', '0005_auto_20180620_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedesc',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作员'),
        ),
    ]