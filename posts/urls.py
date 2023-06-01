from django.urls import path, include

from .views import upvote, downvote

urlpatterns = [
    path('upvote/<int:pk>', upvote, name='upvote'),
    path('downvote/<int:pk>', downvote, name='downvote')
]
