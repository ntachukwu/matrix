from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required, permission_required


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 4
    template_name = 'home.html'
    context = {
        'post_list': queryset,
    }


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post

            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })


@login_required
# @permission_required('request.user.is_authenticated', raise_exception=True)
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.dislike.add(request.user)
    else:
        post.likes.add(request.user)
        post.dislike.remove(request.user)
    post.save()

    return post_detail(request, slug)


@login_required
# @permission_required('request.user.is_authenticated', raise_exception=True)
def dis_like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.dislike.filter(id=request.user.id).exists():
        post.dislike.remove(request.user)
        post.likes.add(request.user)
    else:
        post.dislike.add(request.user)
        post.likes.remove(request.user)
    post.save()

    return post_detail(request, slug)
