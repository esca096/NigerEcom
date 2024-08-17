from django.urls import path
from .views import home, product_list, product_create, product_update
urlpatterns = [
    path('', home, name='home'),
    path('product_list', product_list, name='list'),
    path('product_create', product_create, name='create'),
    path('product_update', product_update, name='update'),
]
