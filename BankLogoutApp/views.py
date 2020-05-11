from django.shortcuts import render
from django.contrib import auth
# Create your views here.

#Function to logout
def LogoutFunction(request):
    auth.logout(request)
    return render(request=request, template_name='html/BankHomeApp/Home_Page.html')

def Admin_LogoutFunction(request):
    auth.logout(request)
    return render(request=request, template_name='html/BankHomeApp/Admin_Home_Page.html')
