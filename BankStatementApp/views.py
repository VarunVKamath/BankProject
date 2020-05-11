from django.shortcuts import render
from TransferMoneyApp.models import BankStatement
# Create your views here.

#Function to display the bank statement of the user.
def BankStatementFunction(request):
	BS_list1=BankStatement.objects.all()
	BS_list=reversed(BS_list1)
	my_dict={'BS_list':BS_list}
	return render(request,template_name='html/TransferMoneyApp/BankStatement.html',context=my_dict)