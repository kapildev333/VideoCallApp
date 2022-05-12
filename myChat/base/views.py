from django.shortcuts import render


# Create your views here.
def render_lobby(request):
    return render(request, 'base/lobby.html')


def render_room(request):
    return render(request, 'base/room.html')
