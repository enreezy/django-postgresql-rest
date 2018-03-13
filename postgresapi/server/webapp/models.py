from django.db import models

# Create your models here.

class Items(models.Model):
	itemname = models.CharField(max_length=200,blank='true')
	quantity = models.CharField(max_length=200,blank='true')
	price = models.CharField(max_length=200,blank='true')

	def __str__(self):
		return self.itemname
