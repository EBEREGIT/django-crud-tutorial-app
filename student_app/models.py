from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students", null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()
    pub_date = models.DateField("date published")
