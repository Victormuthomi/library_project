from django.urls import path

from .views import Booklistview

urlpatterns=[
        path('',Booklistview.as_view(), name='home'), 
]

