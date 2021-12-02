"""Preplite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authApp.views import register, login, profile
from postApp.views import registerUniversity,viewUniversities,registerCompany,registerCompanyUser,viewCompanies,upvote,downvote,viewPosts,createPost,viewComments,addComment,viewCompanyPosts,viewUniversityPosts
from chatApp.views import viewChats,viewParticularChat,sendMessage

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('login/',login),
    path('profile/',profile),
    path('registerUniversity/',registerUniversity),
    path('viewUniversities/',viewUniversities),
    path('viewCompanies/',viewCompanies),
    path('registerCompany/',registerCompany),
    path('registerCompanyUser/',registerCompanyUser),
    path('createPost/',createPost),
    path('upvote/',upvote),
    path('downvote/',downvote),
    path('addComment/',addComment),
    path('viewComments/',viewComments),
    path('viewPosts/',viewPosts),
    path('viewCompanyPosts/',viewCompanyPosts),
    path('viewUniversityPosts/',viewUniversityPosts),
    path('viewChats/',viewChats),
    path('viewParticularChat/',viewParticularChat),
    path('sendMessage/',sendMessage)
]
