# Generated by Django 4.1.1 on 2022-09-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeUser', '0002_remove_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(),
        ),
    ]
