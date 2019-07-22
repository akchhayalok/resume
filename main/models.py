from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
	name = models.CharField('Name',max_length=200)
	dob = models.DateTimeField('D.O.B')
	address = models.TextField('Address')
	email = models.CharField('Email',max_length=200)
	organization = models.CharField('Organization',max_length=200)
	#image = models.ImageField('Image')
    #def __str__(self):
	 #  return self.name