from django.shortcuts import render,redirect
from AccountCreationApp.models import CustomerInfo
from django.contrib import messages
# Create your views here.
def ForgotPass_Page(request):
    if request.method=="POST":
        AC=request.POST['AccountNumber']
        ACN=int(AC)
        Q1=request.POST['Q1']
        Q2=request.POST['Q2']
        Q3=request.POST['Q3']

        q1=CustomerInfo.objects.get(AccountNumber=ACN).Q1
        q2=CustomerInfo.objects.get(AccountNumber=ACN).Q2
        q3=CustomerInfo.objects.get(AccountNumber=ACN).Q3
        y=0

        username=CustomerInfo.objects.get(AccountNumber=ACN).username
        password=CustomerInfo.objects.get(AccountNumber=ACN).password
       

        if (Q1==q1) and (Q2==q2) and (Q3==q3):
            y=1

        if  y!=1:
            messages.info(request,'Invalid Answers')
            return redirect('/login')
        else:
            return redirect('/Change_Password')

    else:
        return render(request,template_name='html/BankLoginApp/Forgot_Password.html',)