from django.db import models
from user.models import User,Customer,Restaurant,Address

# Create your models here.
class Category(models.Model):
     name=models.CharField(max_length=100)

     def __str__(self):
        return self.name

     class meta:
      db_table='FoodCategory'

class SubCategory(models.Model):
    
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
         
    class meta:
      db_table='SubCategory'    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name
    
    class meta:
        db_table='MenuItem'
    


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    is_paid=models.BooleanField(default=False)
    

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'   
    
    class meta:
        db_table='Order'