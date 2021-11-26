from django.shortcuts import render
from .models import MessageModel
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

        messageEntry = MessageModel.objects.create(from_id=from_id,to_id=to_id,timestamp=timestamp,message=message)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewMessages(request):
    json_data = json.loads(request.body)
    from_id = json_data['from_id']
    to_id = json_data['to_id']
    querySet = MessageModel.objects.filter(from_id=from_id,to_id=to_id)
    response = []
    for message in querySet:
        tempList = {}
        tempList['from_id'] = message.from_id
        tempList['to_id'] = message.to_id
        tempList['timestamp'] = message.timestamp
        tempList['message'] = message.message
        response.append(tempList)

    return JsonResponse(response, safe=False)