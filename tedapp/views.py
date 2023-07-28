from django.shortcuts import render, HttpResponse
from tedapp.models import UserAccount
from django.shortcuts import get_object_or_404
from django.conf import settings  
from django.core.mail import send_mail  
import email
from django.contrib import messages


# Create your views here.
def index(request):
     return render(request , "index.html")
def register(request):
     return render(request , "register.html")
def speakers(request):
     return render(request , "speakers.html")
def partners(request):
     return render(request , "partners.html")
def Account(request):
     if request.method == "POST":
      aname = request.POST.get('name')   
      aemail = request.POST.get('email')   
      aphone = request.POST.get('phone')  
      areferral = request.POST.get('referral') 
      acollege = request.POST.get('college')   
      aCity = request.POST.get('City')   
      account=UserAccount(name=aname,email=aemail,phone=aphone,referral=areferral, college=acollege, City=aCity)
      account.save()
     sub = "TEDxIITBOMBAY"
     msg = """Congratulations """ + aname +"""!! \n
You have successfully registered in the TEDxIITBOMBAY \n
Regards, \nAbhyuday"""
     send_mail(
                sub, msg, 'info.tedxiitbombay@gmail.com',[aemail]
            )
     messages.success(request , " You have successfully Registered for TEDxIITBOMBAY")
     return render(request , "index.html")

print("mail sent")