from django.shortcuts import render

# Create your views here.

def Home_Page(request):
	return render(request,template_name='html/BankHomeApp/Home_Page.html')

def Admin_Home_Page(request):
	return render(request,template_name='html/BankHomeApp/Admin_Home_Page.html')