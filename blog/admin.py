from django.contrib import admin
from .models import BlogCategory, Blog, BlogComment

admin.site.site_header = '博客之旅管理后台'  # 设置header
admin.site.site_title = '欢迎来到博客之旅管理后台'   # 设置title
admin.site.index_title = '博客之旅管理后台首页'

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # 在列表页显示字段

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'category', 'author')  # 在列表页显示字段
    list_filter = ('pub_time', 'category')  # 在列表页添加过滤选项
    search_fields = ('title', 'content')  # 添加搜索框搜索字段

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'pub_time', 'blog', 'author')  # 在列表页显示字段
    list_filter = ('pub_time',)  # 在列表页添加过滤选项
    search_fields = ('content',)  # 添加搜索框搜索字段

# 注册模型到后台管理
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)