from django.db import models

# Create your models here.

class Topic(models.Model):
    topi_name = models.CharField(max_length=100,primary_key=True)