# Generated by Django 3.2.9 on 2021-12-01 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_auto_20211115_1813'),
        ('postApp', '0003_auto_20211129_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authApp.usermodel'),
            preserve_default=False,
        ),
    ]
