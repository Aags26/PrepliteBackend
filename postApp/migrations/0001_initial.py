# Generated by Django 3.2.9 on 2021-11-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authApp', '0004_auto_20211115_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('logo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UniversityModel',
            fields=[
                ('university_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('stream_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.IntegerField()),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('content', models.TextField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.companymodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='PostMaterialModel',
            fields=[
                ('material', models.TextField(primary_key=True, serialize=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.postmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUserModel',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('internship', models.BooleanField()),
                ('comapny_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.companymodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.usermodel')),
            ],
        ),
    ]