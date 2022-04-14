from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum

from .models import Orders, Category, Regular_pizza, Topping, Pizza_toppingR, Sicilian_pizza, Pizza_toppingS, Sub, Pasta, Salad, Dinner_platter, Order_counter

#Order counter
counter = Order_counter.objects.first()
if counter==None:
    set_counter=Order_counter(counter=1)
    set_counter.save()

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html",{"message":None})
    
    #Send all the information for the menu
    obj = {
        "regular_pizza": Regular_pizza.objects.all(),
        "sicilian_pizza": Sicilian_pizza.objects.all(),
        "topping": Topping.objects.all(),
        "sub": Sub.objects.all(),
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinner_plate": Dinner_platter.objects.all(),
        "cart": "Empty",
        "price": 0
    }

    return render(request,"menu.html",obj) 

#Login function
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"message": "Invalid Credentials"})
    elif request.method == 'GET':
        return render(request, "login.html", {"message": None})

#Logout function that redirect you to the login page
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged Out"})

#Register Function
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return render(request, "login.html", {"message": "New Account Created"})
    elif request.method == 'GET':
        return render(request, "register.html", {"message": None})

#Display menu view
def menu(request):
    obj = {
        "regular_pizza": Regular_pizza.objects.all(),
        "sicilian_pizza": Sicilian_pizza.objects.all(),
        "topping": Topping.objects.all(),
        "sub": Sub.objects.all(),
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinner_plate": Dinner_platter.objects.all(),
        "cart" : 'Empty',
        "price": 0
    }

    return render(request,"menu.html",obj) 

#Add a new item to the cart
def add(request, categ, name, price, size, cart, actPrice):
    if cart == 'Empty':
        #Replace Empty cart for the content
        cart = "[" + categ + "]" + " " + name + " (" + size + ")"
        print(f"CARTTY {cart}")
        actPrice=price

        #In some cases there's no size, so it just ignore
        cart = cart.replace('(ND)','')

        obj = {
        "regular_pizza": Regular_pizza.objects.all(),
        "sicilian_pizza": Sicilian_pizza.objects.all(),
        "topping": Topping.objects.all(),
        "sub": Sub.objects.all(),
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinner_plate": Dinner_platter.objects.all(),
        "cart" : cart,
        "price": actPrice
        }

        return render(request,"menu.html", obj)
    
    cart += ', ' + "[" + categ + "]" + " " + name + " (" + size + ")"

    #Cart calculation
    auxActPrice = float(actPrice)
    auxPrice = float(price)
    newPrice = auxActPrice + auxPrice
    rPrice = round(newPrice,2)

    pizza = {"type":"Regular Pizza", "name":name, "price":price}
    cart = cart.replace('(ND)','')

    obj = {
        "regular_pizza": Regular_pizza.objects.all(),
        "sicilian_pizza": Sicilian_pizza.objects.all(),
        "topping": Topping.objects.all(),
        "sub": Sub.objects.all(),
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinner_plate": Dinner_platter.objects.all(),
        "cart" : cart,
        "price": rPrice
    }

    return render(request,"menu.html", obj)

#Create a new order function
def create_order_view(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        price = request.POST.get('price')
        count = Order_counter.objects.all()

        #Get last order counter
        if count==None:
            c = Order_counter(counter=1)
            c.save()
        else: 
            c = count.latest('counter')
            c.counter += 1
            c.save()
        user = request.user
        #Create the order with all the components and save it
        order = Orders.objects.create(order_number=c.counter ,desc=cart, priceTot=price, user=user, status="pending")
        order.save()
        return HttpResponseRedirect(reverse("menu"))
    elif request.method == 'GET':
        return HttpResponseRedirect(reverse("menu"))

#Check the orders    
def orders_view(request):
    if  not request.user.is_authenticated:
        return render(request,"login.html",{"message":None})

    #If it's the Admin (SuperUser) it will be able to check all the orders
    if request.user.is_superuser:
        ord = Orders.objects.all()
        obj = {
            "orders": ord
        }
        return render(request, "orders.html", obj)
    user = request.user
    
    #A User will be able to check his own orders
    ord = Orders.objects.filter(user=user)
    obj = {
        "orders": ord
    }
    return render(request, "orders.html", obj)   
        