from django.contrib import admin
from .models import ItemList, Price, Transaction, Cart

# Register your models here.

admin.site.register(ItemList)
admin.site.register(Price)
admin.site.register(Transaction)
admin.site.register(Cart)
