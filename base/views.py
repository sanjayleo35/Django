from django.shortcuts import render
from . models import Room
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

# Create your views here.

