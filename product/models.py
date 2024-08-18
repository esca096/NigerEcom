from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=100000)
    image = models.ImageField(upload_to='image', blank=True)
    slug = models.SlugField(null=True)
    date_time = models.DateTimeField(null=True)
    actif = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
    #cette fonction permet de gerer les liens dynamiques --> "update" est le nom du lien product_update au niveau urls
    def get_absolute_url(self):
        return reverse("update", kwargs={"my_id": self.pk})
    