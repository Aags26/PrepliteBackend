# Generated by Django 3.2.9 on 2021-11-06 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_alter_user_alumni'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserModel',
        ),
    ]
