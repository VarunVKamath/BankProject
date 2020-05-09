from django.shortcuts import render
from AccountCreationApp.models import CustomerInfo
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.

def account_details(request):
    if request.user.is_anonymous ==0: 
        account_info=CustomerInfo.objects.all()
        my_dict={'account_info':account_info}
        return render(request=request, template_name='html/AccountDetailsApp/display.html',context=my_dict)

    else:
        return render(request=request, template_name='html/BankHomeApp/Home_Page.html',)

def Admin_account_details(request):
    if request.user.is_anonymous ==0: 
        account_info=CustomerInfo.objects.all()
        my_dict={'account_info':account_info}
        return render(request=request, template_name='html/AccountDetailsApp/Admin_Dashboard.html',context=my_dict)

    else:
        return render(request=request, template_name='html/BankHomeApp/Admin_Home_Page.html',)
