from django.shortcuts import render
from .serializers import registerserializer,sessionserializer,userpanelserializer
from .models import *
from django.contrib.auth import authenticate
from django.db.models import Q

# Create your views here.

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
from .permissions import IsUser


@api_view(http_method_names=["GET","POST"])
@permission_classes([IsAdminUser])
def createuser(request):
    if request.method == "POST":  
        data=request.data 
        serializer=registerserializer(data=data)
        
        if serializer.is_valid():

            serializer.save()
            a={"message":"successfully created","data":serializer.data}
            
            return Response(data=a)
    else:
        return Response({"msg":"go to post request"})    
    
@api_view(http_method_names=["POST",'GET']) 
@permission_classes([IsAdminUser])
def createsession(request):   
    if request.method == "POST":  
        data=request.data 
        date=data.get("date")
        try:
            a=Session.objects.get(date=date)
            return Response({"msg":"sorry the date is already full try another date"})
        except:
            serializer=sessionserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                a={"message":"successfully session created","data":serializer.data}
                return Response(data=a)
            
    if request.method == "GET": 
        a=Session.objects.all()
        # print(a.values())
        serializer=sessionserializer(instance=a,many=True)
        a={"sessions":serializer.data}
        
        return  Response(data=a) 
    
@api_view(http_method_names=["POST"]) 
@permission_classes([AllowAny])  
def login(request)  :
    if request.method=="POST":
        data=request.data
        username=data.get("username") 
        password=data.get("password")    
        user=authenticate(username=username,password=password)
        
        if user:
            try:
                token = Token.objects.get(user=user)
            except:  
                token = Token.objects.create(user=user)  
            a={"msg":"successfully logged in","token": token.key}
            return Response(data=a)
        else:
             return Response({"msg":"invalid credentilas"})   
         

@api_view(http_method_names=["POST",'GET']) 
@permission_classes([IsAuthenticated])
def monthly_session(request,id):  
    if request.method == "GET": 
        # a=Session.objects.all()
        month=id
        a=Session.objects.filter(date__month=month)
        print(a)
        
        print(a.values())
        serializer=sessionserializer(instance=a,many=True)
        a={"sessions":serializer.data}
        
        return  Response(data=a)      
        
@api_view(http_method_names=["POST",'GET']) 
@permission_classes([IsAuthenticated])
def sessionlist(request):  
    if request.method == "GET": 
        a=Session.objects.all()
        
        print(a)
        
        print(a.values())
        serializer=sessionserializer(instance=a,many=True)
        a={"sessions":serializer.data}
        
        return  Response(data=a) 
    
@api_view(http_method_names=["GET","POST"])
@permission_classes([IsUser,IsAuthenticated])   
def sessionbooking(request):
   
    if request.method == "POST":
        name=request.user
        data = request.data
        print(data)
        title=data.get("title")
        date=data.get("date")
        
        try:
            session = Session.objects.get(Q(title=title) & Q(date=date))
            
        except Session.DoesNotExist:
            return Response({"msg": "Session does not exist"}, status=400)
        
        if session.is_booked==True:
                return Response({"msg":"this session already booked"})
        
        
        serializer_data={
            "sessions":[session.id],
            "user":name.id
        }
        # serializer_data["sessions"]=[session.id]
        # serializer_data["user"]=name.id
        
        serializer=userpanelserializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            session.is_booked=True
            session.save()
            
            return Response({"msg":"session booked successfully","data":serializer.data})
        else:
            return Response({"msg":"enter valid data","data":serializer.errors})
    
    if request.method == "GET":    
        user=request.user  
        a=user_panel.objects.filter(user=user.id)  
        serializer=userpanelserializer(instance=a,many=True)
        return Response(({"data":serializer.data}))
      
        
        
    
                     
        
                
            
     
            
        
           
    
