"""
URL configuration for feedbackSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name='Home'),
    # path("login/",views.Login,name='Login'),
    path("login/",auth_views.LoginView.as_view(template_name='home/login.html'),name='Login'),
    path("logout/",auth_views.LogoutView.as_view(template_name='home/logout.html'),name='Logout'),
    path("register/",views.Register,name='Register'),
    path("profile/",views.profile,name='Profile'),
    # path("FeedBack",views.feedback_view,name='FeedBack'),
    # path("GetReview",views.Review_feedback,name='GetReview'),
    path('Test',views.test,name='Test'),
    path('Submit',views.submit,name='Submit'),
    #report generating 
    path('Score',views.feedback_score_view,name='Score'),
    path('Report',views.feedback_report_view,name='Report'),
   
]
