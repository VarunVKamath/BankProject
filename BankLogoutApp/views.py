from django.shortcuts import render
from django.contrib import auth
# Create your views here.

def LogoutFunction(request):
    auth.logout(request)
    return render(request=request, template_name='html/BankHomeApp/Home_page.html')

def Admin_LogoutFunction(request):
    auth.logout(request)
    return render(request=request, template_name='html/BankHomeApp/Admin_Home_page.html')
