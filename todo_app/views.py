from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer



# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    
    