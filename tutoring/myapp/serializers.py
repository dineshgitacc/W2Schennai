
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class registerserializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=["username","password"]
        
    def create(self, validated_data):
        print(validated_data)
        # password=validated_data.pop("password")
        password=validated_data["password"]
        print(password)
        user=super().create(validated_data)
        
        user.set_password(password)  # this is used to make hash password
        user.save()     
        return user    
        
        
class sessionserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Session
        fields= "__all__"     
        
class userpanelserializer(serializers.ModelSerializer):
   
    class Meta:
        model=user_panel
        fields= "__all__"     
        