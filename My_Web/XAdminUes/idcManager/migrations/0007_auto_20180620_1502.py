# Generated by Django 2.0.5 on 2018-06-20 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idcManager', '0006_imagedesc_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedesc',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作员'),
        ),
    ]
