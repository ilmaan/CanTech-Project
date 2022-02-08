from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

class Portal(View):
    def get(self,request):
        
        return render(request,'portal.html')

class Admin_login(View):
    def get(self,request):
        
        return render(request,'admin_login.html')

class User_login(View):
    def get(self,request):
        
        return render(request,'user_login.html')

class Recruiter_login(View):
    def get(self,request):
        
        return render(request,'recruiter_login.html')



