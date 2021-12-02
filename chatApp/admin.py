from django.contrib import admin
from .models import ChatModel, MessageModel

# Register your mod(els here.
admin.site.register(MessageModel)
admin.site.register(ChatModel)
