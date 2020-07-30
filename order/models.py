from django.db import models
from django.conf import settings

# Create your models here.

PIZZA_SIZE_CHOICES = (
    (1, "small"),
    (2, "medium"),
    (3, "large"),
)

ORDER_STATUS_CHOICES = (
    (1, "not ordered"),
    (2, "being prepared"),
    (3, "chipping"),
    (4, "delivered"),
    (5, "cancelled"),
)


class Pizza(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)

    def __str__(self):
        return f"""order for user '{self.user.username}'"""


class OrderFragment(models.Model):
    quantity = models.IntegerField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_fragment")
    size = models.IntegerField(choices=PIZZA_SIZE_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="fragments")

    def __str__(self):
        return f"""fragment for order '{self.order.id}'"""



