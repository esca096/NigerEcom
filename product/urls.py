from django.urls import path
from .views import home, product_list, product_create, product_update, product_delete, product_table, register, connexion, deconnexion
urlpatterns = [
    path('', home, name='home'),
    path('product_list', product_list, name='list'),
    path('product_create', product_create, name='create'),
    path('product_update/<int:my_id>', product_update, name='update'),
    path('product_delete/<int:my_id>', product_delete, name='delete'),
    path('product_table', product_table, name='table'),
    
    #concerne authenticate signIn & register
    path('register', register, name='register'),
    path('login', connexion, name='login'),
    path('logout', deconnexion, name='logout'),
]
