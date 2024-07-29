from django.shortcuts import render, redirect
from .models import Chatroom

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def chatroom_selection(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    chatrooms = Chatroom.objects.all()
    return render(request, 'chat/roomSelection.html', {'chatrooms': chatrooms})

def create_chatroom(request):
    if request.method == 'POST':
        chatroom_name = request.POST['chatroom_name']
        if chatroom_name:
            Chatroom.objects.create(name=chatroom_name)
    return redirect('chatroom_selection')