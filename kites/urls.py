from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_details/', views.show_details, name='showdetails'),
    path('family_details/', views.family_details, name='familydetails'),
    path('college_details/', views.college_details, name='collegedetails'),

]