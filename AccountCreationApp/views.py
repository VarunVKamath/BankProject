from django.shortcuts import render,redirect
# from AccountCreationApp.forms import CustomerinfoForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import ApprovedAccNumbers
#from django.core.files.storage import FileSystemStorage

#Function To create new users
def New_Acc_Page(request):
    User=get_user_model()
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Age=request.POST['Age']
        Address=request.POST['Address']
        AccountNumber=request.POST['AccountNumber']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']


        Q1=request.POST['Q1']
        Q2=request.POST['Q2']
        Q3=request.POST['Q3']

        # if request.FILES['profilepic']:
        #     profilepic =request.FILES['profilepic']
        #     image=FileSystemStorage()
        #     filename=image.save(profilepic.name,profilepic)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect("/New_Acc")
            elif User.objects.filter(AccountNumber=AccountNumber).exists():
                 messages.info(request,'AccountNumber already registered')
                 return redirect("/New_Acc")
            elif (ApprovedAccNumbers.objects.filter(AccountNumber=AccountNumber).exists())!=1:
                 messages.info(request,'AccountNumber Not Yet Created')
                 return redirect("/New_Acc")
            else:
                user=User.objects.create_user(username=username,password=password1,AccountNumber=AccountNumber,first_name=first_name,last_name=last_name,Age=Age,Address=Address,Q1=Q1,Q2=Q2,Q3=Q3)
                user.save();
                messages.info(request,'user created')
                return redirect("/new_acc")

        else:
             messages.info(request,'passwords not match')
             return redirect("/new_acc")
    else:
        return render(request=request, template_name='html/AccountCreationApp/Account_Creation.html')





        


