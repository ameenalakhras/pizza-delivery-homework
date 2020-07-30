from rest_framework import routers
from django.urls import include, path
from order.views import PizzaAPIViewRoot, PizzaAPIView


app_name = 'order'


urlpatterns = [
    path('pizza', PizzaAPIViewRoot.as_view(), name="pizza"),
    path('pizza/<int:pk>', PizzaAPIView.as_view(), name="pizza_obj"),

]
