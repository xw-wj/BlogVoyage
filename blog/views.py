from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import BlogCategory, Blog, BlogComment
from .forms import PubBlogForm
from django.http.response import JsonResponse
from django.db.models import Q


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', context={'blogs': blogs})


def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)

    except Exception as e:
        blog = None
    return render(request, 'blog_detail.html', context={'blog': blog})


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy("bkauth:login"))
def pub_blog(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'pub_blog.html', context={'categories': categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            # 使用 Django ORM 的 create 方法来创建一个新的 Blog 实例
            # 这个方法接受关键字参数，每个参数对应模型中的一个字段
            # title 参数设置博客的标题，从表单的 cleaned_data 中获取
            # content 参数设置博客的内容，同样从表单的 cleaned_data 中获取
            # category_id 参数设置博客所属的分类的 ID，从表单的 cleaned_data 中获取
            # author 参数设置博客的作者，这里使用 request.user 表示当前登录的用户
            blog = Blog.objects.create(
                title=title,  # 博客标题
                content=content,  # 博客内容
                category_id=category_id,  # 博客分类ID
                author=request.user  # 博客作者，使用当前请求的用户对象
            )
            return JsonResponse({'code': 200, 'message': "博客发布成功!", 'data': {'blog_id': blog.id}})
        else:
            return JsonResponse({'code': 400, 'message': "请检查您的输入!"})


@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(content=content, blog_id=blog_id, author=request.user)
    # 从新加载详情页
    return redirect(reverse('blog:blog_detail', kwargs={'blog_id': blog_id}))


@require_GET
def search(request):
    q = request.GET.get('q')
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).all()
    return render(request, 'index.html', context={'blogs': blogs})
