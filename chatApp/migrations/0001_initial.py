# Generated by Django 3.2.9 on 2021-11-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authApp', '0004_auto_20211115_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('timestamp', models.BigIntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_id', to='authApp.usermodel')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_id', to='authApp.usermodel')),
            ],
        ),
    ]