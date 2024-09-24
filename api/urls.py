from django.urls import path

from .views import BookAPIView, WorkerAPIView

urlpatterns=[
        path('',BookAPIView.as_view()),
        path('workers/', WorkerAPIView.as_view()),
]
