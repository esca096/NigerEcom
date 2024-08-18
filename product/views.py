from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .form import  ProductForm # import rowproductform pour utiliser formulaire robuste
# Create your views here.

def home(request):
    return render(request, 'index.html')


def product_list(request, *args, **kwargs):
    product = Product.objects.all()
    context={
        'products':product
    }
    return render(request, 'products/product_list.html', context)



#Formulaire django rebouste
"""def product_create(request):
    messages = ''
    form = RowProductForm()
    if request.method == 'POST':
        form = RowProductForm(request.POST)
        if form.is_valid():
            new = Product.objects.create(**form.cleaned_data)
            new.save()
            form = RowProductForm()
            messages = "We are receive your product Succefully"
    return render(request, 'products/product_create.html', {'form':form, 'message':messages})"""



    
#Formulaire django simple
'''def product_create(request):
    messages = ''
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We are receive your product Succefully!!!"
    return render(request, 'products/product_create.html', {'form':form, 'message':messages})'''





#Ce formulaire la combinaison du formulaire robuste et simple ---> formulaire complexe
def product_create(request):
    messages = ''
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We are receive your product Succefully!!!"
    return render(request, 'products/product_create.html', {'form':form, 'message':messages})


#Ce code permet d'apporter des modifications a notre formulaire complexe, my_id sert de lien dynamique pour modife de la table
def product_update(request, my_id):
    messages = ''
    
    #cela permet d'ajouter http404  si l'element n'existe pas 1er methode avec possibiliter d'ajouter une page html personnaliser
    '''try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404'''
        
    #2eme methode avec la fonction get_object_or_404
    obj = get_object_or_404(Product, id=my_id)
    
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "Your Product are Modified succefully!!!"
    return render(request, 'products/product_update.html', {'form':form, 'message':messages})


#Creation d'une table pour afficher les produits et  pour faire le CRUD
def product_table(request):
    obj = Product.objects.all()
    return render(request, 'products/product_table.html', {'obj':obj})

#cette fonction permet de faire la suppression des produit
def  product_delete(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    name = obj.name
    if request.method == 'POST':
        obj.delete()
        return redirect('table') # redirection vers la page de table et utiliser le nom du lien product_table
    return render(request, 'products/product_delete.html', {'name':name})