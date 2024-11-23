from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog_detail(request, blog_id):
    return render(request, 'blog_detail.html')


@login_required(login_url=reverse_lazy("bkauth:login"))
def pub_blog(request):
    return render(request, 'pub_blog.html')
