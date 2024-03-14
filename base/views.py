from django.shortcuts import render, redirect
from . models import Room
from .forms import Roomform
'''rooms=[
    {'id': 1 ,'name':'python project'},
    {'id': 2 ,'name':'first project'},
    {'id': 3 ,'name':'my django project'},
]'''


def Home (request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
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



