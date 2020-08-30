from django.urls import path
from . import views


urlpatterns = [
    path('index', views.books_short),
    path('index/result', views.start_lt_3),
]