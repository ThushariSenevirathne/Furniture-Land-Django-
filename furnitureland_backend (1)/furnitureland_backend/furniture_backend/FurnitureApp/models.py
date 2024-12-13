from django.db import models

#user model
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)

#furniture model   
class Furniture(models.Model):
    Id = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=500)
    Price = models.CharField(max_length=500)
    Type = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    ImageUrl = models.CharField(max_length=500)
