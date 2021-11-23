from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    batch = models.SmallIntegerField(null=True)
    alumni = models.BooleanField(null=True)
    phone = models.BigIntegerField()
    profile_image = models.TextField()


    def __str__(self):
        return self.name
