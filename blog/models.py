from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='blog', blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"pk": self.pk})
    