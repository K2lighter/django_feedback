from django.urls import path
from .views import index, done  # hello

urlpatterns = [
    # path('hello', hello),
    path('done', done),
    path('', index),
]
