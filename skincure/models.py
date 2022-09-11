from django.db import models

# Create your models here.
class SkinDisease(models.Model):
    name = models.CharField(max_length = 64, blank = True, null = True)
    description = models.TextField(max_length = 255, blank = True, null = True)
    image = models.ImageField()
    
class Treatment(models.Model):
    description = models.TextField(max_length = 255, blank = True, null= True)