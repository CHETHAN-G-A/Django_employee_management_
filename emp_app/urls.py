from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('update_emp', views.update_emp, name='update_emp'),
    path('update_emp/<int:emp_id>', views.update_emp, name='update_emp'),
    path('update_form_emp', views.update_form_emp, name='update_form_emp'),
    path('update_form_emp/<int:emp_id>', views.update_form_emp, name='update_form_emp'),
    path('del_emp', views.del_emp, name='del_emp'),
    path('del_emp/<int:emp_id>', views.del_emp, name='del_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('signin', views.signin,name='signin'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
]
