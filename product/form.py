from django import forms
from .models import Product

#Formulaire django rebouste
'''class RowProductForm(forms.Form):
    
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': "Enter product's name",
        }
    ))
    
    description = forms.CharField(label='', widget=forms.Textarea(
      attrs={
          'placeholder':"Enter product's description",
          'rows':'2',
          'cols':'20',
          'class':'m1',
          'id':'my_id',
      }  
    ))
    
    price = forms.DecimalField(label='', initial=10, widget=forms.TextInput(
        attrs={
            'placehoalder':"Enter product's price"
        }
    ))
    
    image = forms.ImageField(label='', required=False)
    
    slug = forms.CharField(label='',  widget=forms.TextInput(
        attrs={
            'placeholder':"Enter product's slug"
        }
    ))'''
    
    
    
#Ce formulaire est la plus simple
'''class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'slug')'''
        


#Ce formulaire la combinaison du formulaire robuste et simple ---> formulaire complexe
class ProductForm(forms.ModelForm):
    
    
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': "Enter product's name",
        }
    ))
    
    
    description = forms.CharField(label='', widget=forms.Textarea(
      attrs={
          'placeholder':"Enter product's description",
          'rows':'2',
          'cols':'20',
          'class':'m1',
          'id':'my_id',
      }  
    ))
    
    
    price = forms.DecimalField(label='', initial=10)
    
    
    image = forms.ImageField(label='', required=False)
    
    
    slug = forms.CharField(label='',  widget=forms.TextInput(
        attrs={
            'placeholder':"Enter product's slug"
        }
    ))
    
    
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'slug')
        
        
    # Ces fonctions permettent de poser des conditions au niveaux du formulaire complexe
        
        
    #cette condition permet de verifier PRICE
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get('price')
        if price >= 10:
            return price
        else:
            raise forms.ValidationError('Price must be greater than 10!!! THANKS...') 