from django.shortcuts import render
from .models import MessageModel, ChatModel
from authApp.models import UserModel
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
import time

@csrf_exempt
def sendMessage(request):
    response = {}
    error = False
    if request.method == "POST":
        json_data = json.loads(request.body)

        from_id = json_data['from_id']
        fromUser = UserModel.objects.get(user_id=from_id)
        to_id = json_data['to_id']
        toUser = UserModel.objects.get(user_id=to_id)
        timestamp = json_data['timestamp']
        message = json_data['message_p2p']
        print("here")
        try:
            #chat exists
            # chat = ChatModel.objects.get(Q(from_id=from_id)&Q(to_id=to_id))
            print("here3")
            try:
                chat = ChatModel.objects.get(from_id=fromUser,to_id=toUser)
                print("here2")
                messageEntry = MessageModel.objects.create(from_id=fromUser,to_id=toUser,timestamp=timestamp,message=message,chat_id=chat)
            except:
                print("here5")
                chat = ChatModel.objects.get(from_id=toUser,to_id=fromUser)
                print("here4")
                messageEntry = MessageModel.objects.create(from_id=fromUser,to_id=toUser,timestamp=timestamp,message=message,chat_id=chat)
        except:
            print("here6")
            newChat = ChatModel.objects.create(from_id=fromUser,to_id=toUser)
            messageEntry = MessageModel.objects.create(from_id=fromUser,to_id=toUser,timestamp=timestamp,message=message,chat_id=newChat)
    message = "success"
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewParticularChat(request):
    json_data = json.loads(request.body)
    from_id = json_data['from_id']
    to_id = json_data['to_id']
    querySet = MessageModel.objects.filter((Q(from_id=from_id)&Q(to_id=to_id))|(Q(from_id=to_id)&Q(to_id=from_id))).order_by('timestamp')
    response = {}
    chatList = []
    error = False
    for message in querySet:
        tempList = {}
        tempList['from_id'] = message.from_id.user_id
        tempList['to_id'] = message.to_id.user_id
        tempList['timestamp'] = message.timestamp
        tempList['message_p2p'] = message.message
        chatList.append(tempList)

    result = {}
    result['particular_chat'] = chatList
    response['result'] = result
    message = 'success'
    response['error'] = error
    response['message'] = message

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
    print("here")
    #chats = MessageModel.objects.filter(Q(from_id=user_id)|Q(to_id=user_id)).order_by('-timestamp')
    chatIDSet = []
    chatSet = ChatModel.objects.filter(Q(from_id=user_id)|Q(to_id=user_id))
    for chat in chatSet:
        chatIDSet.append(chat.chat_id)
    fromMessageModel = MessageModel.objects.filter(chat_id__in=chatIDSet).values('chat_id').order_by('-timestamp')
    chats = ChatModel.objects.filter(chat_id__in=fromMessageModel)
    
    for chat in chats:
        userResult = {}
        tempChat = {}
        if chat.from_id.user_id != user_id:
            user = chat.from_id
            userResult['user_id'] = user.user_id
            userResult['name'] = user.name
            userResult['email'] = user.email
            userResult['batch'] = user.batch
            userResult['alumni'] = user.alumni
            userResult['phone'] = user.phone
            userResult['profile_image'] = user.profile_image
        if chat.to_id.user_id != user_id:
            user = chat.to_id
            userResult['user_id'] = user.user_id
            userResult['name'] = user.name
            userResult['email'] = user.email
            userResult['batch'] = user.batch
            userResult['alumni'] = user.alumni
            userResult['phone'] = user.phone
            userResult['profile_image'] = user.profile_image

        tempChat['user'] = userResult
        tempChat['timestamp'] = ''
        # tempList['timestamp'] = chat.timestamp
        # tempList['message'] = chat.message
        chatList.append(tempChat)
        
        

    result = {}
    chat = []
    result['chat'] = chatList
    response['result'] = result
    response['error'] = error
    response['message'] = message  

    return JsonResponse(response)