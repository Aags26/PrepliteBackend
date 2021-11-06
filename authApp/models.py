from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    yearOfStudy = models.SmallIntegerField(null=True)
    alumni = models.BooleanField(null=True)


    def __str__(self):
        return self.name
