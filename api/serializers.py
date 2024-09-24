from rest_framework import serializers 

from books.models import Book 

from workers.models import Worker

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title' ,'subtitle', 'author', 'isbn')

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name', 'id_number', 'member_number')

    
