from django.urls import path
from .views import List_view, Detail_view, Create_view, Update_view, Delete_view

app_name = 'courses'
urlpatterns = [
    path('', List_view.as_view(), name='course-list'),
    path('<int:pk>/course_detail', Detail_view.as_view(), name='course-detail'),
    path('course_create', Create_view.as_view(), name='course-create'),
    path('<int:pk>/course_update', Update_view.as_view(), name='course-update'),
    path('<int:pk>/course_delete', Delete_view.as_view(), name='course-delete'),
]
