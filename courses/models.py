from django.db import models
from django.urls import reverse

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"pk": self.pk})
    