from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from . models import Room,Topic
from .forms import Roomform
'''rooms=[
    {'id': 1 ,'name':'python project'},
    {'id': 2 ,'name':'first project'},
    {'id': 3 ,'name':'my django project'},
]'''

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect("Home")
    
    if request.method=='POST':
        username=request.POST.get('Username').lower()
        password=request.POST.get('Password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'USer does not exits')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,"User name or password doesn't match")
            
    context={'page':page}
    return render(request,'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('Home')

def registerPage(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect("Home")
        else:
            messages.error(request,'An error acquired during the Registration')
    
    return render(request,'base/login_register.html',{'form':form})

def Home (request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(
                              Q(topic__name__icontains=q ) |
                              Q(name__icontains=q) |
                              Q(description__contains=q)
                              )
    topics=Topic.objects.all()
    room_count=rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count,}
    return render(request,'base/Home.html',context)

def room (request,pk):
    '''room=None
    for i in rooms:
        if i ['id'] == int(pk) :
            room=i'''
    room=Room.objects.get(id=pk)
    context={'room':room}        
    return render(request,'base/room.html',context)

@login_required(login_url='/login')
def createRoom(request):
    form=Roomform()
    
    if request.method == 'POST':
        form=Roomform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    
    context={'form':form}
    return render(request,'base/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=Roomform(instance=room)
    
    if request.user != room.host:
        return HttpResponse("you are restricted!!!")
    
    if request.method == 'POST':
        form=Roomform(request.POST,instance=room)
        if form.is_valid():
            form.save() 
            return redirect('Home') 
    context={'form':form}
    return render(request,'base/room_form.html',context)


@login_required(login_url='/login')
def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse("you are restricted!!!")
    
    if request.method=='POST':
        room.delete()
        return redirect('Home')
    return render(request,'base/delete.html',{'obj':room})



