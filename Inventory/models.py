from django.contrib import auth
from django.db import models
from django.urls import reverse

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Category (models.Model):
    Name = models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.Name

class Product (models.Model):
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True)
    Product = models.CharField(max_length=200,blank=False)
    Total_Produced = models.IntegerField()
    Sales = models.IntegerField(default=0)
    Total_Available = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.Product

    @property
    def Save(self):
        return self.Total_Produced - self.Sales

class Rocky_Railway(models.Model):
    Product = models.CharField(max_length=200,blank=False)
    Total_Produced = models.IntegerField()
    Sales = models.IntegerField(default=0)
    Total_Available = models.IntegerField(default=0)

    def __str__(self):
        return 'Product:{0} Total_Produced:{1} Sales:{2} Total_Available:{3} '.format(self.Product, self.Total_Produced, self.Sales, self.Total_Available)

class Roar(Rocky_Railway):
    pass

class Shipwreched(Rocky_Railway):
    pass

class FWN1(Rocky_Railway):
    pass

class FWN2(Rocky_Railway):
    pass

class FWN3(Rocky_Railway):
    pass

class LIFE_OF_JESUS(Rocky_Railway):
    pass

class Leader_Manuals(Rocky_Railway):
    pass

class Student_Books(Rocky_Railway):
    pass

class Friends_with_God_Bible_Story(Rocky_Railway):
    pass
