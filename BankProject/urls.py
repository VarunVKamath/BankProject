"""BankProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from AccountCreationApp import views as ACViews
from AccountDetailsApp import views as ADViews
from BankHomeApp import views as BHViews
from BankLoginApp import views as BLViews
from BankLogoutApp import views as BLoViews
from BankStatementApp import views as BSViews
from ChangePwdApp import views as CPViews
from ForgotPwdApp import views as FPViews
from SecQuestionsApp import views as SQViews
from TransferMoneyApp import views as TMViews


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',BHViews.Home_Page),
    path('Admin_Home/',BHViews.Admin_Home_Page),

    path('New_Acc/', ACViews.New_Acc_Page),

    path('account/',ADViews.account_details),

    path('Admin_Dashboard/',ADViews.Admin_account_details),

    path('login/',BLViews.Login_Page),

    path('Admin_Login/',BLViews.Admin_Login_Page),

    path('logout/', BLoViews.LogoutFunction),

    path('Admin_logout/', BLoViews.Admin_LogoutFunction),

    path('Statement/', BSViews.BankStatementFunction),

    path('Change_Password/', CPViews.Change_Password),

    path('ForgotPassword/', FPViews.ForgotPass_Page),
    
    path('csa/', SQViews.CSA),

    path('Transfer/', TMViews.transfer_money),
   
    

]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)