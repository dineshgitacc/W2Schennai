from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('sessionlist',views.sessionlist,name="sessionlist"),  #url to listout all sesions 
    path('monthly_session/<int:id>/',views.monthly_session,name="sessionlist"),#url to search session for the particular month
    path('sessionbooking',views.sessionbooking,name="sessionbooking") # url to book the session
   
]



