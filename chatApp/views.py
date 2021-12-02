from django.shortcuts import render
from .models import MessageModel,ChatModel
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
import time

@csrf_exempt
def sendMessage(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        from_id = json_data['from_id']
        to_id = json_data['to_id']
        timestamp = time.time()
        message = json_data['message']
        try:
            #chat exists
            chat = ChatModel.objects.get(Q(from_id=from_id)&Q(to_id=to_id))
            messageEntry = MessageModel.objects.create(from_id=from_id,to_id=to_id,timestamp=timestamp,message=message,chat_id=chat.chat_id)
        except:
            newChat = ChatModel.objects.create(from_id=from_id,to_id=to_id)
            messageEntry = MessageModel.objects.create(from_id=from_id,to_id=to_id,timestamp=timestamp,message=message,chat_id=newChat.chat_id)
        
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewParticularChat(request):
    json_data = json.loads(request.body)
    from_id = json_data['from_id']
    to_id = json_data['to_id']
    querySet = MessageModel.objects.filter(from_id=from_id,to_id=to_id).order_by('-timestamp')
    response = []
    for message in querySet:
        tempList = {}
        tempList['from_id'] = message.from_id
        tempList['to_id'] = message.to_id
        tempList['timestamp'] = message.timestamp
        tempList['message'] = message.message
        response.append(tempList)

    return JsonResponse(response, safe=False)

# @csrf_exempt
# def viewChats(request):
#     json_data = json.loads(request.body)
#     user_id = json_data['user_id']
#     response = {}
#     error = False
#     message = "success"
#     result = {}
#     chatList = []
#     chats = MessageModel.objects.filter(Q(from_id=user_id)|Q(to_id=user_id)).order_by('-timestamp')
#     for chat in chats:
#         tempList = {}
#         tempList['from_id'] = chat.from_id
#         tempList['to_id'] = chat.to_id
#         tempList['timestamp'] = chat.timestamp
#         tempList['message'] = chat.message
#         chatList.append(tempList)

#     result['chat'] = chatList
#     response['result'] = result
#     response['error'] = error
#     response['message'] = message

#     return JsonResponse(response)

@csrf_exempt
def viewChats(request):
    json_data = json.loads(request.body)
    user_id = json_data['user_id']
    response = {}
    error = False
    message = "success"
    result = {}
    chatList = []
    #chats = MessageModel.objects.filter(Q(from_id=user_id)|Q(to_id=user_id)).order_by('-timestamp')
    chatIDSet = ChatModel.objects.filter(Q(from_id=user_id)|Q(to_id=user_id))
    fromMessageModel = MessageModel.objects.filter(chat_id__in=chatIDSet).values('chat_id').order_by('-timestamp')
    chats = ChatModel.objects.filter(chat_id__in=fromMessageModel)
    for chat in chats:
        tempList = {}
        tempList['from_id'] = chat.from_id
        tempList['to_id'] = chat.to_id
        tempList['timestamp'] = chat.timestamp
        tempList['message'] = chat.message
        chatList.append(tempList)

    result['chat'] = chatList
    response['result'] = result
    response['error'] = error
    response['message'] = message  