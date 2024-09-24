from django.shortcuts import render

from rest_framework import generics 

from books.models import Book

from workers.models import Worker

from .serializers import BookSerializer, WorkerSerializer

# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

class WorkerAPIView(generics.ListAPIView):
        queryset = Worker.objects.all()
        serializer_class = WorkerSerializer


