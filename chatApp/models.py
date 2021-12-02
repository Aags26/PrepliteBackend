from django.db import models
from django.db.models.fields import related
from authApp.models import UserModel

# Create your models here.
class ChatModel(models.Model):
    from_id = models.IntegerField(primary_key=True)
    from_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='chat_from_id')
    to_id = models.IntegerField(primary_key=True)
    to_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='chat_to_id')
    chat_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.chat_id)

class MessageModel(models.Model):
    from_id = models.IntegerField()
    from_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='message_from_id')
    to_id = models.IntegerField()
    to_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='message_to_id')
    timestamp = models.BigIntegerField()
    message = models.TextField()
    chat_id = models.ForeignKey(ChatModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.from_id)+" "+str(self.to_id)

