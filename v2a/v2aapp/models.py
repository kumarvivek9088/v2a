from django.db import models

# Create your models here.
class feedbackdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.CharField(max_length=500)