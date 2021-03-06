# Generated by Django 2.0.5 on 2018-06-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_auto_20180607_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('comId', models.AutoField(primary_key=True, serialize=False)),
                ('comTime', models.DateTimeField(auto_now_add=True)),
                ('comContent', models.TextField(null=True)),
                ('acId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.BlogAcc')),
            ],
        ),
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('blogId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('publishTime', models.DateTimeField(auto_now_add=True)),
                ('mark', models.TextField(null=True)),
                ('acId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.BlogAcc')),
            ],
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='blogId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.BlogInfo'),
        ),
    ]
