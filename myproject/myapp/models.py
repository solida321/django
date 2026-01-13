from django.db import models


class Login(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=18)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    

class Student(models.Model):
    name=models.CharField(max_length=30) # ==varchar() in database like mysql 
    age=models.PositiveIntegerField() # number
    email=models.EmailField(unique=True) # varchar()
    def __str__(self):
        return f'Name :{self.name} , Age : {self.age} , Email : {self.email}'
    

class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Post Title : {self.title},content : {self.content}'
    


class Customer(models.Model):
    name=models.CharField(max_length=40)
    address=models.TextField()
    def __str__(self):
        return f'Name : {self.name} , Address : {self.address}'
    






    

# Create your models here.
