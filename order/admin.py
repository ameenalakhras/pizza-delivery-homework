from django.contrib import admin
from order.models import Order, OrderFragment, Pizza

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(OrderFragment)
