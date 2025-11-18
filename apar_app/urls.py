from django.urls import path
from .views import index, search_order

urlpatterns = [
    path('', index, name='home'),
    path('search/', search_order, name='search'),
]