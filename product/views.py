from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import UserForm ,  ProductForm # import rowproductform pour utiliser formulaire robuste
from django.contrib import messages

#ces fonction sont dedie au register & sign In
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def product_list(request, *args, **kwargs):
    #ce code gerer la partie des session
    number = request.session.get('visit', 0) + 1
    request.session['visit'] = number
    if number > 4:
        del(request.session['visit'])
    
    #  ce code affiche toute les produit depuis la base de donner
    product = Product.objects.all()
    
    context={
        'products':product,
        'number':number
    }
    
    #ce code gerer la partie les cookies
    reponse = render(request, 'products/product_list.html', context)
    
    username = request.user.username
    password = request.user.password
    reponse.set_cookie('username', username, """max_age=1000""")
    reponse.set_cookie('password', password)
    return reponse



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
@login_required(login_url='login')
def product_create(request):
    messages = ''
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We are receive your product Succefully!!!"
    return render(request, 'products/product_create.html', {'form':form, 'message':messages})


#Ce code permet d'apporter des modifications a notre formulaire complexe, my_id sert de lien dynamique pour modife de la table
@login_required(login_url='login')
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
@login_required(login_url='login')
def product_table(request):
    obj = Product.objects.all()
    return render(request, 'products/product_table.html', {'obj':obj})

#cette fonction permet de faire la suppression des produit
@login_required(login_url='login')
def  product_delete(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    name = obj.name
    if request.method == 'POST':
        obj.delete()
        return redirect('table') # redirection vers la page de table et utiliser le nom du lien product_table
    return render(request, 'products/product_delete.html', {'name':name})




# ces codes geres la partie d'authentification
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was created successfuly')
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, 'products/register.html', {'form':form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Welcome in your page')
            return redirect('list')
        else:
            messages.error(request, 'Worng authenticate')
    return render(request, 'products/login.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')