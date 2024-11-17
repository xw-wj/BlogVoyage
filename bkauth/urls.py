from django.urls import path
from . import views

app_name = 'bkauth'
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email'),
]