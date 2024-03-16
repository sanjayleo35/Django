from django.shortcuts import render, redirect
from django.db.models import Q
from . models import Room,Topic
from .forms import Roomform
'''rooms=[
    {'id': 1 ,'name':'python project'},
    {'id': 2 ,'name':'first project'},
    {'id': 3 ,'name':'my django project'},
]'''

def loginpage(request):
    context={}
    return render(request,'base/login_register.html',context)



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


def createRoom(request):
    form=Roomform()
    if request.method == 'POST':
        form=Roomform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    
    context={'form':form}
    return render(request,'base/room_form.html',context)


def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=Roomform(instance=room)
    if request.method == 'POST':
        form=Roomform(request.POST,instance=room)
        if form.is_valid():
            form.save() 
            return redirect('Home') 
    context={'form':form}
    return render(request,'base/room_form.html',context)

def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('Home')
    return render(request,'base/delete.html',{'obj':room})



