from django.urls import path
from .views import home, product_list, product_create, product_update, product_delete, product_table, register, connexion, deconnexion

#pour pouvoir faire reset du password
from django.contrib.auth import views

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
    
    #pour pouvoir faire reset du password
    path('reset_password', views.PasswordResetView.as_view(template_name='products/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name='products/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='products/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='products/password_reset_done.html'), name='password_reset_complete'),
]
