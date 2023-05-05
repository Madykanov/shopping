from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
# Create your views here.

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        users=None
        try:
            users = User.objects.get(email=email)
        except:
            messages.error(request, 'user does not not exist')
    
        user = authenticate(request, username=users, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist')

    return render(request, 'register/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def to_log(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = User.objects.all()
        # username = request.POST.get('username')
        new_email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if new_email not in email:
            if  password1 == password2:
                if form.is_valid():
                    user = form.save(commit=False)
                    user.email = request.POST.get('email')
                    user.save()
                    return redirect('home')
            else:
                messages.error(request, 'Error password')
            
        else:
            messages.error(request, 'this account already has been registered' )

    return render(request, 'register/to_log.html')



def home(request):
    # q = None
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''
    brand = Brand.objects.all()    
    product = Products.objects.filter(
        Q(title__icontains=q) |
        Q(brand__name__icontains=q) |
        Q(description__icontains=q) 
    )
    
    context = {
        'product':product,
        'brand':brand,
    }
    return render(request, 'body/home.html',context)


def info(request,pk):
    product = Products.objects.get(id=pk)

    products = Products.objects.filter(
        Q(brand__name__icontains=product.brand) 
    )

    context = {
        'product':product,
        'products':products,
    }
    return render(request,'body/info.html',context)


@login_required(login_url='/login')
def addToCart(request,pk):
    products = Products.objects.get(id=pk)
    carts = Cart.objects.filter(
        Q(user__username__icontains=request.user) 
    )
    cart_id = []
    for i in carts:
        cart_id.append(i.product.id)

    if products.id not in cart_id:
        print(cart_id)
        Cart.objects.create(
            user=request.user,
            product = products,
            brand = products.brand,
            title = products.title,
            description = products.description,
            size = products.size,
            price = products.price,
            quant = 1,
            image = products.image,
        )
        return redirect('/')
    else:
        return redirect('/')


def updateCart(request, pk):
    cart = Cart.objects.get(id=pk)
    quant = request.GET.get('quant')

    if request.method == 'GET' and int(quant) != 0:
        cart.quant = request.GET.get('quant')
        cart.save()
        return HttpResponseRedirect ('/mycart')
    else:
        cart.delete()
        return HttpResponseRedirect ('/mycart')


@login_required(login_url='/login')
def mycart(request):
    
    cart = Cart.objects.filter(
        Q(user__username__icontains = request.user)
    )
    total_price = 0
    for price in cart:
        total_price += price.price*price.quant

    context = {
        'cart':cart,
        'total_price':total_price,
    }

    return render(request, 'body/cart.html', context)



def order(request):

    carts = Cart.objects.filter(
        Q(user__username__icontains=request.user)
    )

    for cart in carts:
        Order.objects.create(
            user = cart.user,
            product = cart.product,
            brand = cart.brand,
            title = cart.title,
            description = cart.description,
            size = cart.size,
            price = cart.price*cart.quant,
            quant = cart.quant,
            image = cart.image,
            gender = cart.gender,
        )
        products = Products.objects.get(id=cart.product.id)
        if request.method =='GET':
            products.quant = products.quant-cart.quant
            products.save()
    carts.delete()
    return redirect('/')
    

def myOrder(request):
    order = Order.objects.filter(
        Q(user__username__icontains=request.user)
    )

    context = {
        'order':order,
    }

    return render(request, 'body/order.html', context)




@login_required(login_url='/login')
def favorite(request,pk):
    products = Products.objects.get(id=pk)
    carts = Favorite.objects.filter(
        Q(user__username__icontains=request.user) 
    )
    cart_id = []
    for i in carts:
        cart_id.append(i.product.id)

    if products.id not in cart_id:
        print(cart_id)
        Favorite.objects.create(
            user=request.user,
            product = products,
            brand = products.brand,
            title = products.title,
            description = products.description,
            size = products.size,
            price = products.price,
            quant = 1,
            image = products.image,
        )
        return redirect('/')
    else:
        return redirect('/')
    

def myfavorite(request):
    
    favorite = Favorite.objects.filter(
        Q(user__username__icontains = request.user)
    )
    context = {
        'favorite':favorite,
    }

    return render(request, 'body/favorite.html', context)


def removeFav(request, pk):
    favo = Favorite.objects.get(product=pk)
    print(favo)
    favo.delete()
    return HttpResponseRedirect ('/myfavorite/')