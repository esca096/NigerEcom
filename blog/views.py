from django.shortcuts import get_object_or_404, render
from blog.models import Article
from .form import ArticleForm
from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
    #context_object_name = 'nom_au_choix'   Nom personnalisé pour le contexte
    
    

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)
    
    
class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()
    success_url = '/blog'
    
    '''def form_valid(self, form):
        return super().form_valid(form)'''
    
    
    
class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()
    success_url = '/blog'
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)
    



class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()
    success_url = '/blog'