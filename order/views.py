from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView

from order.serializers import PizzaSerializer
from order.models import Pizza


class PizzaAPIViewRoot(CreateAPIView, ListAPIView):
    queryset = Pizza.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = PizzaSerializer


class PizzaAPIView(RetrieveDestroyAPIView, UpdateAPIView):
    queryset = Pizza.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = PizzaSerializer
