from rest_framework import serializers, status

from authentication.serializers import UserSerializer
from order.models import Pizza, Order, OrderFragment
from pizza_delivery.errors import CustomValidationError
from django.utils.translation import ugettext_lazy as _


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class EditOrderSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display', read_only=True)
    default_error_messages = {
        'cant_update_delivered': _("You can't change a delivered order."),
    }

    class Meta:
        model = Order
        exclude = ('user', )

    def validate(self, attrs):

        if self.instance.status == 4:
            raise CustomValidationError(
                self.default_error_messages['cant_update_delivered'],
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        else:
            return super(EditOrderSerializer, self).validate(attrs)


class OrderFragmentSerializer(serializers.ModelSerializer):
    size_name = serializers.CharField(source='get_size_display', read_only=True)
    pizza_name = serializers.CharField(source='pizza.name', read_only=True)

    class Meta:
        model = OrderFragment
        fields = "__all__"


class EditOrderFragmentSerializer(OrderFragmentSerializer):
    default_error_messages = {
        'cant_update_delivered': _("You can't change a delivered order."),
    }

    def validate(self, attrs):
        if self.instance.order.status == 4:
            raise CustomValidationError(
                self.default_error_messages['cant_update_delivered'],
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        else:
            return super(EditOrderFragmentSerializer, self).validate(attrs)

    class Meta:
        model = OrderFragment
        exclude = ("order",)
