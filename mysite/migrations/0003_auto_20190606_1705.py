# Generated by Django 2.2.1 on 2019-06-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wealth',
            field=models.IntegerField(default=50),
        ),
    ]
