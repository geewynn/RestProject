from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurants, Menu
from .forms import addForm, menuForm

# Create your views here.


def showRestaurants(request):
    all_rest = Restaurants.objects.all()
    context = {'all_rest': all_rest}
    return render(request, 'restaurants.html', context)
 

def addRestaurants(request):
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants')
    else:
        form = addForm()
        context = {'form': form}
        return render(request, 'addRestaurant.html', context)


def editRestaurants(request, id):
    rest = get_object_or_404(Restaurants, pk=id)
    if request.method == 'POST':
        form = addForm(request.POST, instance=rest)
        if form.is_valid():
            form.save()
            return redirect('restaurants')
    else:
        form = addForm(instance=rest)
        context = {'form': form}
        return render(request, 'editRestaurant.html', context)


def deleteRestaurants(request, id):
    rest = get_object_or_404(Restaurants, pk=id)
    rest.delete()

    return redirect('restaurants')


def showMenu(request, id):
    menu = Menu.objects.all()
    context = {'all_menu': menu}
    return render(request, 'menu.html', context)


def addMenu(request, id):
    if request.method == 'POST':
        form = menuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu', id=id)
    else:
        form = menuForm()
        context = {'form': form}
    return render(request, 'addMenu.html', context)


def editMenu(request, id):
    menu = get_object_or_404(Menu, pk=id)
    if request.method == 'POST':
        form = menuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu', id=id)
    else:
        form = menuForm(instance=menu)
        context = {'form': form}
        return render(request, 'editMenu.html', context)


def deleteMenu(request, id):
    menu = get_object_or_404(Menu, pk=id)
    menu.delete()

    return redirect('restaurants')
