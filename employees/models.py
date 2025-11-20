from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task
    
'''class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=111)
    photo=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name'''