from django.db import models
from django.db.models.fields.related import ForeignKey
from authApp.models import UserModel

# Create your models here.
class CompanyModel(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return str(self.company_id)

class CompanyUserModel(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_id = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)
    user_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    internship = models.BooleanField()

    def __str__(self):
        return str(self.company_id)+" - "+str(self.user_id)

class UniversityModel(models.Model):
    university_id = models.AutoField(primary_key=True)
    name = models.TextField()
    stream_name = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return str(self.university_id)

class PostModel(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    timestamp = models.IntegerField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    content = models.TextField()
    company_id = models.IntegerField(null=True)
    company_id = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)
    university_id = models.IntegerField(null=True)
    university_id = models.ForeignKey(UniversityModel,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post_id)

class CommentModel(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    post_id = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    timestamp = models.IntegerField()
    content = models.TextField()
    user_id = models.IntegerField()
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment_id)

class PostMaterialModel(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_id = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    material = models.TextField(primary_key=True)

    def __str__(self):
        return self.material




