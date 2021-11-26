# Generated by Django 3.2.9 on 2021-11-26 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.IntegerField()),
                ('content', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.postmodel')),
            ],
        ),
    ]
