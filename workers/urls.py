from django.urls import path 
from .views import Workerlistview

urlpatterns = [
        path('workers/', Workerlistview.as_view()),
]
