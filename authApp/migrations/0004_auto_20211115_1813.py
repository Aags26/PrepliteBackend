# Generated by Django 3.2.9 on 2021-11-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_rename_user_usermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='yearOfStudy',
            new_name='batch',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='id',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='phone',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='profile_image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
