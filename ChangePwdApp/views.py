from django.shortcuts import render,redirect
from AccountCreationApp.models import CustomerInfo
from django.contrib import messages 
from django.contrib.auth.models import auth,User
from django.contrib.auth.hashers import make_password
# Create your views here.

#Function to change the password if the user has forgot the password.
def Change_Password(request):
    ACN=request.session['number']
    if request.method=="POST":
        password1=request.POST['password3']
        password2=request.POST['password4']

        if password1==password2:
            password3=make_password(password1)
            CustomerInfo.objects.filter(AccountNumber=ACN).update(password=password3)
            messages.info(request,'password changed')
            auth.logout(request)
            return redirect("/login")
        else:
            auth.logout(request)
            messages.info(request,'passwords dont match plz try again')
            return redirect('/login')

    else:
        return render(request,template_name='html/BankLoginApp/Change_Password.html',)

#Function to change the password if the user is logged in.
def Change_Password2(request):
    if request.method=="POST":
        current_user=request.user
        ACN=current_user.AccountNumber
        password1=request.POST['password3']
        password2=request.POST['password4']

        if password1==password2:
            password3=make_password(password1)
            CustomerInfo.objects.filter(AccountNumber=ACN).update(password=password3)
            messages.info(request,'password changed')
            return redirect("/change_pass")
        else:
            messages.info(request,'passwords dont match plz try again')
            return redirect('/change_pass')

    else:
        return render(request,template_name='html/BankLoginApp/Change_Password.html',)