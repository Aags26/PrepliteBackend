from django.db import models
from authApp.models import UserModel

# Create your models here.
class MessageModel(models.Model):
    from_id = models.IntegerField(primary_key=True)
    from_id = models.ForeignKey(UserModel)
    to_id = models.IntegerField(primary_key=True)
    to_id = models.ForeignKey(UserModel)
    timestamp = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    
    def __str__(self):
        return self.from_id,self.to_id
