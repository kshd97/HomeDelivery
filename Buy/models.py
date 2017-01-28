from __future__ import unicode_literals
from django.db import models
from Login.models import Customer
from Login_Store.models import Store 

class ItemList(models.Model):
	p_id = models.AutoField(primary_key =  True)
	p_name = models.CharField(max_length=30)
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.p_name

class Price(models.Model):
	p_id = models.ForeignKey(ItemList)
	store_id = models.ForeignKey(Store)
	Price = models.DecimalField(max_digits=4,decimal_places=2)


class Cart(models.Model):
	c_id = models.ForeignKey(Customer)
	p_id = models.IntegerField()
	quantity = models.IntegerField()
	preference = models.CharField(max_length=20)


class Transaction(models.Model):
	c_id = models.ForeignKey(Customer)
	price_id = models.ForeignKey(Price)
	quantity = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)

	