from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/article_detail', ArticleDetailView.as_view(), name='article-detail'),
    path('article_create', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/article_update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/article_delete', ArticleDeleteView.as_view(), name='article-delete'),
]
