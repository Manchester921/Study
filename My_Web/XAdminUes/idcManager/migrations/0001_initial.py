# Generated by Django 2.0.5 on 2018-06-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('create_time', models.DateTimeField()),
            ],
        ),
    ]