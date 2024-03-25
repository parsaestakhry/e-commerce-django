from django.db import models

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
    
    def __str__(self) -> str:
        return self.first_name + " - " + self.last_name
    
    
class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.id + ":" + self.customer
    

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    purchase = models.ManyToManyField(Purchase)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name
    
    



class Manager(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    
    def __str__(self) -> str:
        return self.name
    
    
    
    

     

    
    