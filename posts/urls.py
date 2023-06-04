from django.urls import path, include

from .views import upvote, downvote, PostDetailView

urlpatterns = [
    path('upvote/<int:pk>', upvote, name='upvote'),
    path('downvote/<int:pk>', downvote, name='downvote'),
    path('<int:pk>', PostDetailView.as_view(), name="post_detail")
]
