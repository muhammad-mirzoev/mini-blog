from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .models import Post
from .forms import PostCreateForm


def post_list_view(request):
    posts = (
        Post.objects
        .published()
        .select_related('author')
    )

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )


def post_detail_view(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author'),
        slug=slug,
        status=Post.Status.PUBLISHED
    )

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )


@login_required
@require_http_methods(['GET', 'POST'])
def post_create_view(request):
    form = PostCreateForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        messages.success(
            request,
            'Пост успешно создан'
        )
        return redirect(
            'blog:detail',
            slug=post.slug
        )

    return render(
        request,
        'blog/post_form.html',
        {
            'form': form,
            'title': 'Создание поста',
        }
    )


@login_required
@require_http_methods(['GET', 'POST'])
def post_edit_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return HttpResponseForbidden(
            'Вы не можете редактировать этот пост'
        )

    form = PostCreateForm(
        request.POST or None,
        request.FILES or None,
        instance=post
    )

    if form.is_valid():
        form.save()
        messages.success(
            request,
            'Пост обновлён'
        )
        return redirect(
            'blog:detail',
            slug=post.slug
        )

    return render(
        request,
        'blog/post_form.html',
        {
            'form': form,
            'title': 'Редактирование поста',
        }
    )
