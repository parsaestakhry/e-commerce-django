from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    date_created = models.DateField(auto_now_add=True)
    hello = models.CharField(max_length=100,default="hello")
    pic = models.ImageField(upload_to='images/', default="")
    
    def __str__(self) -> str:
        return self.first_name + " - " + self.last_name
    
    
class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    customer = models.OneToOneField(User, on_delete=models.CASCADE, default=100)
    
    def __str__(self) -> str:
        return str(self.id)
    

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='images/', default="")
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    purchase = models.ManyToManyField(Purchase)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=0)
    pic = models.ImageField(upload_to='images/', default="")
    description = models.CharField(max_length=500, default="")
    
    def __str__(self) -> str:
        return self.name
    
    
class Manager(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    
    def __str__(self) -> str:
        return self.first_name
    
    
class purhase_product_user(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
    
    
    
    
    

     

    
    