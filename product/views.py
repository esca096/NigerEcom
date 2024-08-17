from django.shortcuts import render
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


#Ce code permet d'apporter des modifications a notre formulaire complexe
def product_update(request):
    messages = ''
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "Your Product are Modified succefully!!!"
    return render(request, 'products/product_update.html', {'form':form, 'message':messages})