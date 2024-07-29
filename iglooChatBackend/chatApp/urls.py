from django.urls import path, include
from chatApp import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

from .consumer import ChatConsumer

urlpatterns = [
    # path("", chat_views.chatPage, name="chat-page"),
    path('', chat_views.chatroom_selection, name='chatroom_selection'),
    path('create/', chat_views.create_chatroom, name='create_chatroom'),
    path('chat/<int:chatroom_id>/', chat_views.chatPage, name='chatroom'),
    # authentication section
    path("auth/login/", LoginView.as_view
         (template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]


