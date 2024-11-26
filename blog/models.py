from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='分类名称')

    def __str__(self):
        return self.name  # 后台显示的名称

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.title  # 后台显示的名称

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name


class BlogComment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='博客')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.content  # 后台显示的名称

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name
