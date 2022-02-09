from email import message
from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

class Portal(View):
    def get(self,request):
        
        return render(request,'portal.html')

class Admin_login(View):
    def get(self,request):
        
        return render(request,'admin_login.html')

class User_login(View):
    def post(self,request):
        if request.method == 'POST':
            uname = request.POST['uname']
            uemail = request.POST['uemail']
            uphno = request.POST['uphno']
            psswd = request.POST['psswd']
            type = "Applicant"
            try:
               user = User.objects.create(uname=uname,uemail=uemail,uphno=uphno,psswd=psswd,type=type)
               return render(request,'signup.html',{uname:'uname',uemail:'uemail',uphno:'uphno',psswd:'psswd',type:'type'})
            except:
                message = messages.error(request, 'User Already Exists')
                return render(request,'user_login.html',message)   
        

    def get(self,request):
        
        return render(request,'user_login.html')

class Recruiter_login(View):
    def get(self,request):
        
        return render(request,'recruiter_login.html')



