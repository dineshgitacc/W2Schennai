from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    is_booked = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
class user_panel(models.Model) :
    user=models.OneToOneField(User,on_delete=models.CASCADE)  
    sessions=models.ManyToManyField(Session,related_name="session")
    
    def __str__(self) :
        return self.user.username
    
    
    
    
    
    
  
