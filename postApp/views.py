from django.core.checks.messages import Error
from django.shortcuts import render
from .models import UniversityModel,CompanyUserModel,CompanyModel,PostModel,PostMaterialModel,CommentModel
from django.http import JsonResponse, HttpResponse
from authApp.models import UserModel
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
import time

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
    response = {}
    result = {}
    universityList = []
    for university in querySet:
        tempList = {}
        tempList['university_id'] = university.university_id
        tempList['name'] = university.name
        tempList['stream_name'] = university.stream_name
        universityList.append(tempList)

    result['university'] = universityList
    response['result'] = result
    response['error'] = False
    response['message'] = 'success'
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

        companyEntry = CompanyModel.objects.create(name=companyName,logo=companyLogo)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewCompanies(request):
    error = False
    message = "success"
    querySet = CompanyModel.objects.all()
    response = {}
    result = {}
    companyList = []
    
    for company in querySet:
        tempList = {}
        tempList['company_id'] = company.company_id
        tempList['name'] = company.name
        tempList['logo'] = company.logo
        companyList.append(tempList)

    result['company'] = companyList
    response['result'] = result
    response['error'] = error
    response['message'] = message
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

        companyUserEntry = CompanyUserModel.objects.create(company_id=company_id,user_id=user_id,internship=internship)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewPosts(request):
    error = False
    message = "success"
    response = {}
    result = {}
    postList = []
    querySet = PostModel.objects.all().order_by('-timestamp')
    for post in querySet:
        tempList = {}
        tempList['post_id'] = post.post_id
        tempList['timestamp'] = post.timestamp
        tempList['upvotes'] = post.upvotes
        tempList['downvotes'] = post.downvotes
        tempList['content'] = post.content

        user = post.user_id
        userResult = {}
        userResult['user_id'] = user.user_id
        userResult['name'] = user.name
        userResult['email'] = user.email
        userResult['batch'] = user.batch
        userResult['alumni'] = user.alumni
        userResult['phone'] = user.phone
        userResult['profile_image'] = user.profile_image
        tempList['user'] = userResult

        companyResult = {}
        try :
            company = post.company_id
            companyResult['company_id'] = company.company_id
            companyResult['name'] = company.name
            companyResult['logo'] = company.logo
        except CompanyModel.DoesNotExist:
            companyResult = {}

        tempList['company'] = companyResult

        universityResult = {}
        try:
            university = post.university_id
            universityResult['university_id'] = university.university_id
            universityResult['name'] = university.name
            universityResult['stream_name'] = university.stream_name
        except UniversityModel.DoesNotExist:
            universityResult = {}

        tempList['university'] = universityResult

        postList.append(tempList)

    result['post'] = postList
    response['result'] = result
    response['error'] = error
    response['message'] = message
    return JsonResponse(response, safe=False)

@csrf_exempt
def createPost(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        timestamp = time.time()
        user_id = json_data['user_id']
        upvotes = 0
        downvotes = 0
        content = json_data['content']
        university_id = json_data['university_id']
        company_id = json_data['company_id']
        user = UserModel.objects.get(user_id=user_id)
        company = CompanyModel.objects.get(company_id=company_id)
        university = UniversityModel.objects.get(university_id=university_id)

        postEntry = PostModel.objects.create(university_id=university,company_id=company,user_id=user,upvotes=upvotes,downvotes=downvotes,content=content,timestamp=timestamp)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def upvote(request):
    response = {}
    result = {}
    error = False
    message = "success"
    if request.method=="POST":
        json_data = json.loads(request.body)

        post_id = json_data['post_id']
        postObject = PostModel.objects.get(post_id=post_id)
        postObject.upvotes = postObject.upvotes + 1
        postObject.save()

    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def downvote(request):
    response = {}
    result = {}
    error = False
    message = "success"
    if request.method=="POST":
        json_data = json.loads(request.body)

        post_id = json_data['post_id']
        postObject = PostModel.objects.get(post_id=post_id)
        postObject.downvotes = postObject.downvotes + 1
        postObject.save()

    response['error'] = error
    response['message'] = message

    return JsonResponse(response)

@csrf_exempt
def viewComments(request):
    error = False
    message = "success"
    json_data = json.loads(request.body)
    post_id = json_data['post_id']
    post = PostModel.objects.get(post_id=post_id)
    response = {}
    result = {}
    commentList = []
    querySet = CommentModel.objects.filter(post_id=post_id).order_by('-timestamp')
    for comment in querySet:
        tempList = {}
        tempList['comment_id'] = comment.comment_id
        tempList['content'] = comment.content
        tempList['timestamp'] = comment.timestamp

        userList = {}
        userList['user_id'] = comment.user_id.user_id
        userList['name'] = comment.user_id.name
        userList['email'] = comment.user_id.email
        userList['batch'] = comment.user_id.batch
        userList['alumni'] = comment.user_id.alumni
        userList['phone'] = comment.user_id.phone
        userList['profile_image'] = comment.user_id.profile_image

        tempList['user'] = userList
        commentList.append(tempList)

    result['comment'] = commentList
    response['result'] = result
    response['error'] = error
    response['message'] = message
    return JsonResponse(response, safe=False)

@csrf_exempt
def addComment(request):
    response = {}
    error = False
    message = "success"
    if request.method == "POST":
        json_data = json.loads(request.body)

        post_id = json_data['post_id']
        post = PostModel.objects.get(post_id=post_id)
        content = json_data['content']
        timestamp = time.time()
        user_id = json_data['user_id']
        user = UserModel.objects.get(user_id=user_id)

        commentEntry = CommentModel.objects.create(post_id=post,content=content,timestamp=timestamp,user_id=user)
    response['error'] = error
    response['message'] = message

    return JsonResponse(response)