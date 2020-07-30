from rest_framework import routers
from django.urls import include, path
from order.views import PizzaAPIViewRoot, PizzaAPIView, OrderAPIView, OrderAPIViewRoot, \
    OrderFragmentAPIViewRoot, OrderFragment, OrderFragmentAPIView

app_name = 'order'


urlpatterns = [
    path('pizza', PizzaAPIViewRoot.as_view(), name="pizza"),
    path('pizza/<int:pk>', PizzaAPIView.as_view(), name="pizza_obj"),

    path('order', OrderAPIViewRoot.as_view(), name="order"),
    path('order/<int:pk>', OrderAPIView.as_view(), name="order_obj"),

    path("order_fragment", OrderFragmentAPIViewRoot.as_view(), name="order_fragment"),
    path("order_fragment/<int:pk>", OrderFragmentAPIView.as_view(), name="order_fragment_obj"),

]
