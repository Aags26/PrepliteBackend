from django.shortcuts import render
from .models import UniversityModel,CompanyUserModel,CompanyModel,PostModel,PostMaterialModel
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

@csrf_exempt
def registerUniversity(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        universityName = json_data['name']
        streamName = json_data['stream_name']

        universityEntry = UniversityModel.objects.create(name=universityName,stream_name=streamName)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewUniversities(request):
    querySet = UniversityModel.objects.all()
    response = []
    for university in querySet:
        tempList = {}
        tempList['university_id'] = university.university_id
        tempList['name'] = university.name
        tempList['stream_name'] = university.stream_name
        response.append(tempList)

    return JsonResponse(response, safe=False)


# endpoint for adding company
@csrf_exempt
def registerCompany(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        companyName = json_data['name']
        companyLogo = json_data['logo']

        universityEntry = CompanyModel.objects.create(name=companyName,logo=companyLogo)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewCompanies(request):
    querySet = CompanyModel.objects.all()
    response = []
    for company in querySet:
        tempList = {}
        tempList['company_id'] = company.company_id
        tempList['name'] = company.name
        tempList['logo'] = company.logo
        response.append(tempList)

    return JsonResponse(response, safe=False)

@csrf_exempt
def registerCompanyUser(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        company_id = json_data['company_id']
        user_id = json_data['user_id']
        internship = json_data['internship']

        universityEntry = UniversityModel.objects.create(company_id=company_id,user_id=user_id,internship=internship)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)
