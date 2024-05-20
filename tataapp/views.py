from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages, auth
from decimal import Decimal 
from tataapp.forms import Update_Newcars
from tataapp.models import FeaturedCars, NewCars
from tataapp.forms import Update_FeaturedCars
from django.http import HttpResponseNotAllowed

# Create your views here.

def index(request):
    obj = NewCars.objects.all()
    car = FeaturedCars.objects.all()
    return render(request,'index.html',{'obj':obj, 'car':car})

def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('adminindex')
        else:
            messages.error(request,'invalid username or password')
            return render (request,'admin/adminlogin.html')
    return render(request,'admin/adminlogin.html')

def adminindex(request):
    return render(request, 'admin/adminindex.html')
 

def addcars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = Decimal(request.POST.get('price'))
        image = request.FILES.get('image')
        newcars = NewCars(name=name, desc=desc, price=price, image=image)
        newcars.save()
        return redirect('addcars')
    return render(request, 'admin/addcars.html')

def newcars(request):
    obj = NewCars.objects.all()
    return render(request,'admin/newcars.html',{'obj':obj})

def add_featuredcars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = Decimal(request.POST.get('price'))
        image = request.FILES.get('image')
        featuredcars = FeaturedCars(name=name, desc=desc, price=price, image=image)
        featuredcars.save()
        return redirect('add_featuredcars')
    return render(request, 'admin/addfeaturedcars.html')


def car_details(request, car_id):
    car = get_object_or_404(NewCars, pk=car_id)
    return render(request, 'admin/viewnew.html', {'car': car})

def updatenewcars(request, pk):
    car = get_object_or_404(NewCars, pk=pk)
    form = Update_Newcars(instance=car)
    if request.method == 'POST':
        form = Update_Newcars(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('newcars')  
    return render(request, 'admin/update_newcar.html', {'form': form, 'car': car})


def featuredcars(request):
    car = FeaturedCars.objects.all()
    return render(request,'admin/featuredcars.html', {'car':car })


def featuredcar_details(request, car_id):
    car = get_object_or_404(FeaturedCars, pk=car_id)
    return render(request, 'admin/viewfeaturedcars.html', {'car': car})


def edit_featuredcar(request, car_id):
    car = get_object_or_404(FeaturedCars, pk=car_id)
    form = Update_FeaturedCars(instance=car)
    if request.method == 'POST':
        form = Update_FeaturedCars(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('featuredcars')
    return render(request, 'admin/updatefeaturedcar.html', {'form': form, 'car': car})

def viewfeatured(request, car_id):
    car = get_object_or_404(FeaturedCars, pk=car_id)
    return render(request, 'viewfeatured.html', {'car': car})


def viewnewcars(request, car_id):
    car = get_object_or_404(NewCars, pk=car_id)
    return render(request, 'viewnewcars.html', {'car': car})


def delete_car(request, car_id):
    if request.method == 'POST':
        car = get_object_or_404(FeaturedCars, pk=car_id)
        car.delete()
        return redirect('featuredcars')
    else:
        return HttpResponseNotAllowed(['POST'])


def delete_newcar(request, car_id):
    if request.method == 'POST':
        car = get_object_or_404(NewCars, pk=car_id)
        car.delete()
        return redirect('newcars')
    else:
        return HttpResponseNotAllowed(['POST'])
    
    