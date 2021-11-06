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
        userEmail = json_data['email']
        userName = json_data['name']
        userPassword = hashlib.md5(bytes(json_data['password'].encode())).hexdigest()
        userYearOfStudy = json_data['yearOfStudy']
        userAlumni = json_data['alumni']

        if userAlumni=='y':
            userAlumni = True
        else:
            userAlumni = False

        userEntry = UserModel.objects.create(name=userName,email=userEmail,password=userPassword,yearOfStudy=userYearOfStudy,alumni=userAlumni)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def login(request):
    response = {}
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            user = UserModel.objects.get(Q(email=json_data['email']),Q(password=hashlib.md5(bytes(json_data['password'].encode())).hexdigest()))
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
    error = False
    message = 'success'
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            user = UserModel.objects.get(email=json_data['email'])
            response['name'] = user.name
            response['email'] = user.email
            response['yearOfStudy'] = user.yearOfStudy
            response['alumni'] = user.alumni
        except UserModel.DoesNotExist:
            error = True
            message = 'failure'
            response['error'] = error
            response['message'] = message
            return JsonResponse(response)
        
    response['error'] = error
    response['message'] = message
    return JsonResponse(response)