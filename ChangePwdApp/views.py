from django.shortcuts import render,redirect
from AccountCreationApp.models import CustomerInfo
from django.contrib import messages 
from django.contrib.auth.hashers import make_password
# Create your views here.
def Change_Password(request):
    if request.method=="POST":
        AC=request.POST['AccountNumber']
        ACN=int(AC)
        password1=request.POST['password3']
        password2=request.POST['password4']

        if password1==password2:
            password3=make_password(password1)
            CustomerInfo.objects.filter(AccountNumber=ACN).update(password=password3)
            messages.info(request,'password changed')
            return redirect("/login")
        else:
            messages.info(request,'passwords dont match plz try again')

    else:
        return render(request,template_name='html/BankLoginApp/Change_Password.html',)