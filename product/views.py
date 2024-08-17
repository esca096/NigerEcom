from django.shortcuts import render
from .models import Product
from .form import RowProductForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def product_list(request, *args, **kwargs):
    product = Product.objects.all()
    context={
        'products':product
    }
    return render(request, 'products/product_list.html', context)


def product_create(request):
    messages = ''
    form = RowProductForm()
    if request.method == 'POST':
        form = RowProductForm(request.POST)
        if form.is_valid():
            new = Product.objects.create(**form.cleaned_data)
            new.save()
            messages = "We are receive your product Succefully"
    return render(request, 'products/product_create.html', {'form':form, 'message':messages})