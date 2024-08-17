from django import forms
from .models import Product

#la meilleur façon de faire un formulaire robuste
class RowProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    slug = forms.CharField()
    
    
    
#Ce formulaire est la plus basique
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'slug')