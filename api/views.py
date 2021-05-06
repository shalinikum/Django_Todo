from django.shortcuts import render

# Create your views here.

from rest_framework import generics

# Create your views here.
from task import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TodoSerializer
