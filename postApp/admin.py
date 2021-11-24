from django.contrib import admin
from .models import CompanyModel,CompanyUserModel,PostMaterialModel,PostModel,UniversityModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(CompanyUserModel)
admin.site.register(PostModel)
admin.site.register(PostMaterialModel)
admin.site.register(UniversityModel)