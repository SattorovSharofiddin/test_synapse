from django.urls import path
from .views import SendMessageView, CreateRoomView

urlpatterns = [
    path('send_message/', SendMessageView.as_view(), name='send_message'),
    path('create_room/', CreateRoomView.as_view(), name='create_room'),
]
