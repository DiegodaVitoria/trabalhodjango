from django.urls import path
from.views import index, list, confirma

urlpatterns = [
    path('', index),
    path('list', list),
    path('confirma', list),


]