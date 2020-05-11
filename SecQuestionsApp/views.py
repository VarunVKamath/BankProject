from django.shortcuts import render
from AccountCreationApp.models import CustomerInfo
# Create your views here.

#Function to change the security answers.
def CSA(request):
    CSA_list=CustomerInfo.objects.all()
    my_dict={'CSA_list':CSA_list}
    if request.method=="POST":
        Q1=request.POST['Q1']
        Q2=request.POST['Q2']
        Q3=request.POST['Q3']

        User=request.user
        
        CustomerInfo.objects.filter(AccountNumber=User.AccountNumber).update(Q1=Q1,Q2=Q2,Q3=Q3)
        messages.info(request, 'Changed')
        return render(request=request, template_name='html/AccountDetailsApp/CSA.html',context=my_dict)

    else:
        return render(request=request, template_name='html/AccountDetailsApp/CSA.html',context=my_dict)