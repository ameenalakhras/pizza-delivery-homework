from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView

from order.serializers import PizzaSerializer, OrderSerializer, EditOrderSerializer, OrderFragmentSerializer, \
    EditOrderFragmentSerializer
from order.models import Pizza, Order, OrderFragment


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


class OrderAPIViewRoot(CreateAPIView, ListAPIView):
    queryset = Order.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = OrderSerializer


class OrderAPIView(RetrieveDestroyAPIView, UpdateAPIView):
    queryset = Order.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if (self.request.method == 'PATCH') or (self.request.method == 'PUT'):
            serializer_class = EditOrderSerializer

        return serializer_class


class OrderFragmentAPIViewRoot(CreateAPIView, ListAPIView):
    queryset = OrderFragment.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = OrderFragmentSerializer


class OrderFragmentAPIView(RetrieveDestroyAPIView, UpdateAPIView):
    queryset = OrderFragment.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = OrderFragmentSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if (self.request.method == 'PATCH') or (self.request.method == 'PUT'):
            serializer_class = EditOrderFragmentSerializer

        return serializer_class
