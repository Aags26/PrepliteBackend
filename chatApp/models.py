from django.db import models
from django.db.models.fields import related
from authApp.models import UserModel

# Create your models here.
class MessageModel(models.Model):
    from_id = models.IntegerField(primary_key=True)
    from_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='from_id')
    to_id = models.IntegerField(primary_key=True)
    to_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='to_id')
    timestamp = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    
    def __str__(self):
        return str(self.from_id)+" "+str(self.to_id)
