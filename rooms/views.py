from django.shortcuts import render
rooms = [
    {'id':1, 'name':'Python for beginers'},
    {'id':2, 'name':'Ddjango for beginers'},
    {'id':3, 'name':'Javascript for beginers'},
]


# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html',context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'room.html', context)