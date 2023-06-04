from django.shortcuts import render
from django.views.generic import DetailView

from .models import PostVote, Post


def upvote(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        post_interaction = PostVote.objects.get(post=post, user=request.user)
    except PostVote.DoesNotExist:
        post_interaction = PostVote(post=post, user=request.user, vote=1)
        post_interaction.save()
        post.karma = post.karma + 1
        post.save()
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})

    if post_interaction.vote == 1:
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})
    else:
        post_interaction.switch_vote()
        post.karma = post.karma + 2
        post.save()
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})


def downvote(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        post_interaction = PostVote.objects.get(post=post, user=request.user)
    except PostVote.DoesNotExist:
        post_interaction = PostVote(post=post, user=request.user, vote=-1)
        post_interaction.save()
        post.karma = post.karma - 1
        post.save()
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})

    if post_interaction.vote == -1:
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})
    else:
        post_interaction.switch_vote()
        post.karma = post.karma - 2
        post.save()
        return render(request, 'ajax/upvote.html', context={'karma': post.karma})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
