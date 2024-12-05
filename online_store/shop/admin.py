from django.contrib import admin
from .models import Category, Product, DeliveryMethod, Order,OrderAdmin


admin.site.register(Category,)
admin.site.register(Product)
admin.site.register(DeliveryMethod)
admin.site.register(Order,OrderAdmin)
