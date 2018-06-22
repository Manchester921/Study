# Generated by Django 2.0.5 on 2018-06-20 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.BookCategory', verbose_name='图书馆类别'),
            preserve_default=False,
        ),
    ]
