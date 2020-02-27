# Generated by Django 2.0.5 on 2018-06-20 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=64, verbose_name='图书名称')),
                ('image', models.ImageField(storage=system.storage.ImageStorage(), upload_to='')),
                ('publish', models.CharField(max_length=64, verbose_name='出版社')),
                ('author', models.CharField(max_length=64, verbose_name='作者')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='录入时间')),
                ('bookcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='图书馆类别')),
            ],
            options={
                'verbose_name': '图书管理',
                'verbose_name_plural': '图书管理',
            },
        ),
    ]