from django.shortcuts import render
from .models import UserModel
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
import hashlib

@csrf_exempt
def register(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        userName = json_data['name']
        userEmail = json_data['email']
        userPassword = hashlib.md5(bytes(json_data['password'].encode())).hexdigest()
        userBatch = json_data['batch']
        userAlumni = json_data['alumni']
        userPhone = json_data['phone']
        userProfileImage = json_data['profile_image']

        if userAlumni=='y':
            userAlumni = True
        else:
            userAlumni = False

        userEntry = UserModel.objects.create(name=userName,email=userEmail,password=userPassword,batch=userBatch,alumni=userAlumni,phone=userPhone,profile_image=userProfileImage)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def login(request):
    response = {}
    result = {}
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            userResult = {}
            user = UserModel.objects.get(Q(email=json_data['email']),Q(password=hashlib.md5(bytes(json_data['password'].encode())).hexdigest()))
            userResult['user_id'] = user.user_id
            userResult['name'] = user.name
            userResult['email'] = user.email
            userResult['batch'] = user.batch
            userResult['alumni'] = user.alumni
            userResult['phone'] = user.phone
            userResult['profile_image'] = user.profile_image
            result['user'] = userResult
            response['result'] = result
        except UserModel.DoesNotExist:
            error = True
            message = 'failure'
            response['error'] = error
            response['message'] = message
            return JsonResponse(response)
      
    response['error'] = error
    response['message'] = message
    return JsonResponse(response)

@csrf_exempt
def profile(request):
    response = {}
    result = {}
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            userResult = {}
            user = UserModel.objects.get(user_id=json_data['user_id'])
            userResult['user_id'] = user.user_id
            userResult['name'] = user.name
            userResult['email'] = user.email
            userResult['batch'] = user.batch
            userResult['alumni'] = user.alumni
            userResult['phone'] = user.phone
            userResult['profile_image'] = user.profile_image
            result['user'] = userResult
            response['result'] = result
        except UserModel.DoesNotExist:
            error = True
            message = 'failure'
            response['error'] = error
            response['message'] = message
            return JsonResponse(response)
        
    response['error'] = error
    response['message'] = message
    return JsonResponse(response)

@csrf_exempt
def viewUsers(request):
    response = {}
    result = {}
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)

        userList = UserModel.objects.filter(~Q(user_id=json_data['user_id']))

        users = []

        for user in userList:
            userResult = {}
            userResult['user_id'] = user.user_id
            userResult['name'] = user.name
            userResult['email'] = user.email
            userResult['batch'] = user.batch
            userResult['alumni'] = user.alumni
            userResult['phone'] = user.phone
            userResult['profile_image'] = user.profile_image
            users.append(userResult)

        result['chat'] = users
        response['result'] = result
        
    response['error'] = error
    response['message'] = message
    return JsonResponse(response)

@csrf_exempt
def profileImage(request):
    response = {}
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)

        user = UserModel.objects.get(user_id=json_data['user_id'])
        user.profile_image = json_data['profile_image']
        user.save()
        
    response['error'] = error
    response['message'] = message
    return JsonResponse(response)