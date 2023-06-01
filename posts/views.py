from django.shortcuts import render

from .models import PostInteraction, Post


def upvote(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        post_interaction = PostInteraction.objects.get(post=post, user=request.user)
    except PostInteraction.DoesNotExist:
        post_interaction = PostInteraction(post=post, user=request.user, vote=1)
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
        post_interaction = PostInteraction.objects.get(post=post, user=request.user)
    except PostInteraction.DoesNotExist:
        post_interaction = PostInteraction(post=post, user=request.user, vote=-1)
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
