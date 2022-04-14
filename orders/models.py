from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
    
    def create_category(self, name):
        category = self.create(name=name)
        return category


class Regular_pizza(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"


class Sicilian_pizza(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Topping(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Pizza_toppingR(models.Model):
    pizza=models.ForeignKey(Regular_pizza,on_delete=models.CASCADE)
    topping=models.ForeignKey(Topping,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pizza} - {self.topping}"

class Pizza_toppingS(models.Model):
    pizza=models.ForeignKey(Sicilian_pizza,on_delete=models.CASCADE)
    topping=models.ForeignKey(Topping,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pizza} - {self.topping}"

class Sub(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Pasta(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Salad(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Dinner_platter(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Orders(models.Model):
    order_number=models.IntegerField()
    desc=models.CharField(max_length=256,default='')
    priceTot=models.DecimalField(max_digits=4,decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=64,default='initiated')

    def __str__(self):
        return f"{self.order_number} - {self.status} - {self.priceTot}"

class Order_counter(models.Model):
    counter=models.IntegerField()

    def __str__(self):
        return f"Order no: {self.counter}  "
