from rest_framework import serializers, status
from order.models import Pizza, Order


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"
