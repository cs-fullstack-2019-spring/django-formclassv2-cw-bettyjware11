from django.urls import path

from . import views
# setting paths within application...1 path for each function request...
urlpatterns = [
    path('', views.index, name='index'),
    path('applicationForm/', views.applicationForm, name='applicationForm'),
    path('listEmployeeInfo/', views.listEmployeeInfo, name='listEmployeeInfo'),
    path('application/', views.application, name='application'),
]