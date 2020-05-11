from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from AccountCreationApp.models import CustomerInfo
from .models import BankStatement

#Function to send the money and update the bank statement.
def transfer_money(request):
	current_user=request.user
	current_balance=current_user.Balance
	Current_ACC_NO=current_user.AccountNumber
	current_user_name=current_user.first_name+current_user.last_name
	if request.method=="POST":
		AC=request.POST['AccountNumber']
		ACN=int(AC)
		AM=request.POST['Amount']
		AMO=int(AM)

		if (CustomerInfo.objects.filter(AccountNumber=ACN).exists())!=1:
			messages.info(request,'account Does not exist')
			return redirect('/transfer')


		elif (current_balance < AMO):
			messages.info(request,'Insufficient Balance')
			return redirect('/transfer')

		elif (ACN==Current_ACC_NO):
			messages.info(request,'Cannot Send to self')
			return redirect('/transfer')
		
		else:

			New_Balance=current_balance-AMO
			Receiver_Balance=CustomerInfo.objects.get(AccountNumber=ACN).Balance
			Receiver_Name=CustomerInfo.objects.get(AccountNumber=ACN).first_name+CustomerInfo.objects.get(AccountNumber=ACN).last_name

			New_Receiver_Balance=Receiver_Balance+AMO


			CustomerInfo.objects.filter(AccountNumber=Current_ACC_NO).update(Balance=New_Balance)
			CustomerInfo.objects.filter(AccountNumber=ACN).update(Balance=New_Receiver_Balance)

			BankStatement.objects.create(
			Sender=current_user_name,
			Receiver=Receiver_Name,
			Sender_acc=Current_ACC_NO,
			Receiver_acc=ACN,
			Transaction_Value=AMO,
			Sender_Balance=New_Balance,
			Receiver_Balance=New_Receiver_Balance,

						)

			messages.info(request,'Transaction Successful!')
			return redirect('/transfer')



	return render(request,template_name='html/TransferMoneyApp/Transfer_money.html',)






