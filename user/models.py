from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here


class Address(models.Model):
      
      Name=models.CharField(max_length=50,null=True)
      city=models.CharField(max_length=100,null=True)
      state=models.CharField(max_length=100,null=True)
      area=models.CharField(max_length=100,null=True)
      landmark=models.CharField(max_length=100,null=True)
      Pincode=models.IntegerField(null=True)
      latitude=models.IntegerField(null=True)
      longitude=models.IntegerField(null=True)



class User(AbstractUser): 
    is_Customer = models.BooleanField(default=False,null=True)
    is_restaurant = models.BooleanField(default=False,null=True)
    Address=models.ForeignKey( Address,on_delete=models.CASCADE,null=True)
    Phone_no = models.IntegerField(null=True)
    Website=models.CharField(max_length=100,null=True)
    Restaurant_name=models.CharField(max_length=100,null=True)    

   
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username    
    
    
class Customer(models.Model):
     Name=models.CharField(max_length=100,null=True)
     Email=models.EmailField(null=True)
     Address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

     class Meta:
          db_table='Customer'
     def __str__(self) :
          return self.Name

class Restaurant(models.Model):
     Name=models.CharField(max_length=100,null=True)
     Email=models.EmailField(default=True,null=True)     
     Website=models.URLField(null=True)
     Address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

     class Meta:
          db_table='Restaurant'
     def __str__(self) :
          return self.Name  



