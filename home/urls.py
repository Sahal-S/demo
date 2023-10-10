from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),       # login page
    path('check/',views.check,name='check'),      
    path('success_c/',views.success_c,name='success_c'),    # successful login
    path('success_e/',views.success_e,name='success_e'),
    path('signup_as/',views.signup_as,name='signup_as'),    # signup page
    path('signup_e/',views.signup_e,name='signup_e'),       #redirect to signup as employe
    path('signup_c/',views.signup_c,name='signup_c'),       #redirect to signup as company
    path('log_out_c/',views.log_out_c,name='log_out_c'),
    path('log_out_e/',views.log_out_e,name='log_out_e'),
    path('dropdown/',views.dropdown,name='dropdown'),
    path('droptest/',views.droptest,name='droptest'),
    path('test/',views.test,name='test'),
    path('dlt/',views.dlt,name='dlt'),
    path('add/',views.add,name='add'),
    path('modify/',views.modify,name='modify'),
    path('power/',views.power,name='power')
      ]
