from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()
    pub_date = models.DateField("date published")
