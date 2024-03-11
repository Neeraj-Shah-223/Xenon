from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page, name="login"),
    path('login', views.login_page, name="login"),
    path('signup', views.signup_page, name="signup"),
    path('contact', views.contact_page, name="contact"),
    # path('contact_us/', views.contact_us_submit, name='contact_us_submit')
]
