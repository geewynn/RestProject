# Generated by Django 2.2.2 on 2019-08-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20190826_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
