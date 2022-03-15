from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from job.views import *
from django.contrib.auth.models import User
from job.models import *
# Create your views here.


class Home(View):
    def get(self,request):
        
        return render(request,'home.html')

    def post(self,request):
        if request.method == 'POST':
            f_name = request.POST['name']
            f_phoneno = request.POST['phoneno']
            f_email = request.POST['email']
            f_message = request.POST['message']

            feedback = FeedbackModel.objects.create(f_name=f_name,f_phoneno=f_phoneno,f_email=f_email,f_message=f_message)
        
        return render(request,'home.html')     
      
class ComingSoon(View):
    def get(self,request):
        
        return render(request,'comingsoon.html')

class Services(View):
    def get(self,request):
        
        return render(request,'services.html')

class Contact(View):
    def get(self,request):
        
        return render(request,'contact.html')

class Developer(View):
    def get(self,request):

        if not request.user.is_authenticated:
            return redirect('job/user-login')
        else:
            user = request.user
            print(user.username,'POPOPOPO')
            cuser = UserModel.objects.get(uemail=user.username)
            allusers = UserModel.objects.all()
                
            return render(request,'developers.html',{'cuser':cuser,'allusers':allusers})

class Recruiter(View):
    def get(self,request):

        if not request.user.is_authenticated:
            return redirect('job/user-login')
        else:
            w = request.GET.get('who') 
            user = request.user
            cuser = RecruiterModel.objects.get(remail=user.username)
            if w == 'users':
                data = UserModel.objects.all()
                return render(request,'recruiter-user.html',{'cuser':cuser,'data':data})
            elif w == 'recruiter':
                data = RecruiterModel.objects.all()
                return render(request,'recruiter-user.html',{'cuser':cuser,'data':data})
                
            return render(request,'recruiter.html',{'cuser':cuser})

class FeedbackForm(View):
    def post(self,request):
        print("1")
        if request.method == 'POST':
            print("2")
            f_name = request.POST['name']
            f_phoneno = request.POST['phoneno']
            f_email = request.POST['email']
            f_message = request.POST['message']

            feedback = FeedbackModel.objects.create(f_name=f_name,f_phoneno=f_phoneno,f_email=f_email,f_message=f_message)
        
        return redirect('home')

class AboutUs(View):
    def get(self,request):
        
        return render(request,'about_us.html')


class GetQuote(View):
    def post(self,request):
        if request.method == 'POST':
            qname = request.POST['qname']
            qphone = request.POST['qphone']
            qemail = request.POST['qemail']
            qbussiness = request.POST['qbussiness']
            totalpage = request.POST['totalpage']
            stack = request.POST['stack']
            qbudget = 0
            qteam = request.POST['qteam']
            qtype = request.POST['qtype']
            

            feedback = QuotationModel.objects.create(qname=qname,qphone=qphone,qemail=qemail,qbussiness=qbussiness,totalpage=totalpage,stack=stack,qbudget=qbudget,qteam=qteam,qtype=qtype)
        return redirect('home') 
