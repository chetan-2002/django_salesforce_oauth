
from django.urls import path
from . import views

urlpatterns = [
    path('login_with_salesforce/', views.login_with_salesforce, name='login_with_salesforce'),
    path('salesforce/callback/', views.oauth_callback, name='oauth_callback'),
    path('welcome/', views.welcome, name='welcome'),
]