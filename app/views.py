from django.shortcuts import render

# Create your views here.

def login(request):
    
    context = {
    }

    return render(request, 'app/login.html', context)

def signup(request):

    context = {
    }

    return render(request, 'app/signup.html', context)

def dashboard(request):

    context = {
    }

    return render(request, 'app/dashboard.html', context)

def transactions(request):

    context = {
    }
    
    return render(request, 'app/transactions.html', context)

def quotation(request):

    context = {
    }
    
    return render(request, 'app/quotation.html', context)

def inventory(request):

    context = {
    }
    
    return render(request, 'app/inventory.html', context)

def material(request):

    context = {
    }
    
    return render(request, 'app/material.html', context)

def delivery(request):

    context = {
    }
    
    return render(request, 'app/delivery.html', context)