# django博客搭建

### 1.创建项目

- 用pycharm直接创建。

- 命令行创建app

  ```python
  python manage.py startapp blog
  ```

  

### 2.配置

手动在blog中创建urls.py文件

![image-20241117113935052](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\image-20241117113935052.png)

![1731814826566](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731814826566.png)

![1731814864955](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731814864955.png)

然后在django项目里的urls进行配置，并在templates里面创建index.html

![1731814944667](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731814944667.png)

![1731814968846](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731814968846.png)

创建static目录，把bootstrap文件夹放进去

如果不想每次手动在html文件写{%load static%}，在setting里面加入
![1731817005035](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731817005035.png)

然后配置静态文件加载路径

```python
STATIC_URL = 'static/'
#静态文件加载路径
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

```

### 3.首页导航条

- 先去官网，点击Example

![1731817693327](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731817693327.png)

- 下拉点击header

![1731817729581](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731817729581.png)

- 右击检查，找到你要的header，然后点击复制outerHtml

  index

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>博客之旅</title>
    <link rel="stylesheet" href="{% static 'bootstrap-5.3.3-dist/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap-5.3.3-dist/popper.min.js' %}"></script>
    <script src="{% static 'bootstrap-5.3.3-dist/js/bootstrap.min.js' %}"></script>
</head>
<body>
<header class="p-3 text-bg-dark">
    <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap">
                    <use xlink:href="#bootstrap"></use>
                </svg>
            </a>

            <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><a href="#" class="nav-link px-2 text-secondary">Home</a></li>
                <li><a href="#" class="nav-link px-2 text-white">Features</a></li>
                <li><a href="#" class="nav-link px-2 text-white">Pricing</a></li>
                <li><a href="#" class="nav-link px-2 text-white">FAQs</a></li>
                <li><a href="#" class="nav-link px-2 text-white">About</a></li>
            </ul>

            <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
                <input type="search" class="form-control form-control-dark text-bg-dark" placeholder="Search..."
                       aria-label="Search">
            </form>

            <div class="text-end">
                <button type="button" class="btn btn-outline-light me-2">Login</button>
                <button type="button" class="btn btn-warning">Sign-up</button>
            </div>
        </div>
    </div>
</header>
</body>
</html>
```

![1731822075091](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731822075091.png)

因为要展示logo所以把下面删掉。搞成

```html
 <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap">
                    <use xlink:href="#bootstrap"></use>
                </svg>
```

```html
<img src="{% static 'image/logo-mi2.png' %}" alt="" height="40">
```

加个下面边框，更立体
![1731823570777](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731823570777.png)

![1731823589052](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731823589052.png)

下面是调整过后的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>博客之旅</title>
    <link rel="stylesheet" href="{% static 'bootstrap-5.3.3-dist/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap-5.3.3-dist/popper.min.js' %}"></script>
    <script src="{% static 'bootstrap-5.3.3-dist/js/bootstrap.min.js' %}"></script>
</head>
<body>
<header class="p-3 text-bg-light border-bottom" >
    <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
               <img src="{% static 'image/logo-mi2.png' %}" alt="" height="40">
            </a>

            <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><a href="#" class="nav-link px-2 text-secondary">首页</a></li>
                <li><a href="#" class="nav-link px-2 text-secondary">发布博客</a></li>
            </ul>

            <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
                <input type="search" class="form-control  text-bg-light" placeholder="搜索..."
                       aria-label="Search">
            </form>

            <div class="text-end">
                <button type="button" class="btn btn-outline-primary me-2">登录</button>
                <button type="button" class="btn btn-primary">注册</button>
            </div>
        </div>
    </div>
</header>
</body>
</html>
```

![1731823932831](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731823932831.png)

首页添加背景，在static里面建立css文件夹，然后建立base.css文件，然后导入

![1731824353924](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731824353924.png)

![1731824399724](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731824399724.png)

效果图
![1731824438962](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731824438962.png)

 然后需要做个容器，来放发布的博客

- 先去bootstrap找Containers

![1731824941213](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731824941213.png)

![1731825113110](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731825113110.png)

产生了问题，距离导航条太近  例如：

![1731825157356](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731825157356.png)

解决：

![1731825298639](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731825298639.png)

让博客列表这几个字上下左右都有点间隔，并且容器四个角都变成园的

![1731825534431](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731825534431.png)

效果：

![1731825589949](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731825589949.png)

在容器里面加入卡片，因为咱的布局是在博客列表下面，然后一行两个卡片布局，所以要用下面方法


```html
<div class="row row-cols-2">
    <div class="col">
        <div class="card text-center">
            <div class="card-header">
                Featured
            </div>
            <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
            <div class="card-footer text-body-secondary">
                2 days ago
            </div>
        </div>
    </div>
</div>
```

row-cols-2代表一行两列

中间卡片是复制的bootstrap

![1731826571303](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731826571303.png)

下面是代码

```html
<main class="container bg-white p-2 rounded">
    <h1>博客列表</h1>
    <div class="row row-gap-2"> <!-- 移除 row-cols-2 -->
        <!-- 第一个卡片 -->
        <div class="col-md-6">
            <div class="card text-center">
                <div class="card-header">
                    Featured
                </div>
                <div class="card-body">
                    <h5 class="card-title">Special title treatment</h5>
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                <div class="card-footer text-body-secondary">
                    2 days ago
                </div>
            </div>
        </div>
        <!-- 第二个卡片 -->
        <div class="col-md-6">
            <div class="card text-center">
                <div class="card-header">
                    Featured
                </div>
                <div class="card-body">
                    <h5 class="card-title">Special title treatment</h5>
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                <div class="card-footer text-body-secondary">
                    2 days ago
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card text-center">
                <div class="card-header">
                    Featured
                </div>
                <div class="card-body">
                    <h5 class="card-title">Special title treatment</h5>
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                <div class="card-footer text-body-secondary">
                    2 days ago
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card text-center">
                <div class="card-header">
                    Featured
                </div>
                <div class="card-body">
                    <h5 class="card-title">Special title treatment</h5>
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                <div class="card-footer text-body-secondary">
                    2 days ago
                </div>
            </div>
        </div>
    </div>
</main>
```

效果：

![1731827116004](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731827116004.png)

然后改成自己需要的，把居中删掉，固定卡片大小，使它不会因为内容而改变大小

![image-20241117154736170](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\image-20241117154736170.png)

修改后代码，以及效果

```html
<main class="container bg-white p-2 rounded">
    <h1>博客列表</h1>
    <div class="row row-gap-4"> <!-- 移除 row-cols-2 -->
        <!-- 第一个卡片 -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <a href="#">Django 基础知识</a>
                </div>
                <div class="card-body " style="height: 100px">
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                </div>
                <div class="card-footer text-body-secondary d-flex justify-content-between">
                    <div>
                        <img src="{% static 'image/avatar.jpeg' %}" class="rounded-circle" width="30" height="30" alt="">
                        wwj
                    </div>
                    <div>发布时间: 2024年11月17日  11:28</div>
                </div>
            </div>
        </div>
        <!-- 第二个卡片 -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <a href="#">Django 基础知识</a>
                </div>
                <div class="card-body " style="height: 100px">
                    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                </div>
                <div class="card-footer text-body-secondary d-flex justify-content-between">
                    <div>
                        <img src="{% static 'image/avatar.jpeg' %}" class="rounded-circle" width="30" height="30" alt="">
                        wwj
                    </div>
                    <div>发布时间: 2024年11月17日  11:28</div>
                </div>
            </div>
        </div>

    </div>
</main>
```

![1731829726820](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731829726820.png)

### 4.博客详情页

- 写view.py

```python
def blog_detail(request，blog_id):
    return render(request, 'blog_detail.html')
```

- 写urls.py

```python
path('blog/<blog_id>', views.blog_detail, name='blog_detail'),
```

- 在templates创建blog_detail.html文件

  - 把index.html文件内容复制过去，然后对齐先简单修改，主要把main里面的改了

    ![1731830675901](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731830675901.png)

![1731839073163](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731839073163.png)

下面是效果
![1731839416762](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731839416762.png)

接下来做用户评论列表，打开bootstrap5，搜索list group

![1731840653218](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731840653218.png)

选这种带下划线的复制下来
![1731844909566](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731844909566.jpg)

### 5.发布博客详情页

- 老规矩，创建view.py
  ```python
  def pub_blog(request):
      return render(request, 'pub_blog.html')
  ```

  

- 配置urls
  ```python
  urlpatterns = [
      path('', views.index, name='index'),
      path('blog/detail/<blog_id>', views.blog_detail, name='blog_detail'),
      path('blog/pub', views.pub_blog, name='pub_blog'),
  
  ]
  
  ```

  

- 创建pub_blog.html，并把index内容复制过去，在进行修改,还是只修改main

```html
<main class="container bg-white p-2 rounded">
    <h1>发布博客</h1>
    <div class="mt-3">
        <form action="" method="post">
            <div class="mb-3">
                <label class="form-label">标题</label>
                <input type="text" name="title" class="form-control">
            </div>
            <div class="mb-3">
                <label class="form-label">分类</label>
                <select name="category" class="form-select">
                    <option value="1">python</option>
                    <option value="2">前端</option>
                    <option value="3">人工智能</option>
                </select>
            </div>
            <div class="mb-3">
                <label class="form-label">内容</label>
                <div id="editor—wrapper">
                    <div id="toolbar-container"><!-- 工具栏 --></div>
                    <div id="editor-container"><!-- 编辑器 --></div>
                </div>
            </div>
        </form>
    </div>
    <div class="mt-3 text-end">
        <button type="submit" class="btn btn-primary">提交</button>
    </div>

</main>
```

![1731848125865](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731848125865.png)

怎样弄内容编辑器呢，这里使用的是https://www.wangeditor.com/ 这个编辑器

- 下载wangeditor的js与css文件，并在head上面导入

![1731848836314](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731848836314.png)

- 把下面的style写在引入下面

```html
<style>
  #editor—wrapper {
    border: 1px solid #ccc;
    z-index: 100; /* 按需定义 */
  }
  #toolbar-container { border-bottom: 1px solid #ccc; }
  #editor-container { height: 500px; }
</style>
```

- 写个js文件，并且也引入
  ![1731848967042](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731848967042.png)

```javascript
window.onload = function () {
    const {createEditor, createToolbar} = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        }
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })
}
```

### 6.登陆注册页面

- 在创建一个app因为登录注册属于授权了，所以创建个bkauth

```python
python manage.py startapp bkauth
```

- 注册qpp，在app里面创建urls文件，还有view文件

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'bkauth'
  urlpatterns = [
      path('login', views.login, name='login'),
      path('register', views.register, name='register'),
  ]
  ```

```python
from django.shortcuts import render

# Create your views here.
def login(request):
    return  render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
```

还有在大的urls里面添加东西

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('auth/', include('bkauth.urls')),
]
```

- 在templates里面分别创建login.html、register.html,并把index.html文件代码复制获取并做修改

login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>博客之旅</title>
    <link rel="stylesheet" href="{% static 'bootstrap-5.3.3-dist/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap-5.3.3-dist/popper.min.js' %}"></script>
    <script src="{% static 'bootstrap-5.3.3-dist/js/bootstrap.min.js' %}"></script>
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
</head>
<body>
<header class="p-3 text-bg-light border-bottom mb-2">
    <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                <img src="{% static 'image/logo-mi2.png' %}" alt="" height="40">
            </a>

            <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><a href="#" class="nav-link px-2 text-secondary">首页</a></li>
                <li><a href="#" class="nav-link px-2 text-secondary">发布博客</a></li>
            </ul>

            <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
                <input type="search" class="form-control  text-bg-light" placeholder="搜索..."
                       aria-label="Search">
            </form>

            <div class="text-end">
                <button type="button" class="btn btn-outline-primary me-2">登录</button>
                <button type="button" class="btn btn-primary">注册</button>
            </div>
        </div>
    </div>
</header>
<main class="container bg-white p-2 rounded">
    <div style="max-width: 330px" class="m-auto">
       <h1 class="text-center">登录</h1> 
        <form method="post" action="">
            <div class="mb-3">
                <label>邮箱</label>
                <input type="email" class="form-control" name="email" placeholder="邮箱">
            </div>
            <div class="mb-3">
                <label>密码</label>
                <input type="password" class="form-control" name="password" placeholder="密码">
            </div>
            <div class="form-check mb-3">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    记住我
                </label>
            </div>
            <div class="mb-3">
                <button class="btn btn-primary w-100">登录</button>
            </div>
        </form>
    </div>
</main>

</body>
</html>
```

![1731851709124](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731851709124.png)

效果：

![1731851932895](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731851932895.png)

register.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>博客之旅</title>
    <link rel="stylesheet" href="{% static 'bootstrap-5.3.3-dist/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap-5.3.3-dist/popper.min.js' %}"></script>
    <script src="{% static 'bootstrap-5.3.3-dist/js/bootstrap.min.js' %}"></script>
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
</head>
<body>
<header class="p-3 text-bg-light border-bottom mb-2">
    <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                <img src="{% static 'image/logo-mi2.png' %}" alt="" height="40">
            </a>

            <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><a href="#" class="nav-link px-2 text-secondary">首页</a></li>
                <li><a href="#" class="nav-link px-2 text-secondary">发布博客</a></li>
            </ul>

            <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
                <input type="search" class="form-control  text-bg-light" placeholder="搜索..."
                       aria-label="Search">
            </form>

            <div class="text-end">
                <button type="button" class="btn btn-outline-primary me-2">登录</button>
                <button type="button" class="btn btn-primary">注册</button>
            </div>
        </div>
    </div>
</header>
<main class="container bg-white p-2 rounded">
    <div style="max-width: 330px" class="m-auto">
        <h1 class="text-center">注册</h1>
        <form method="post" action="">
            <div class="mb-3">
                <label>用户名</label>
                <input type="text" class="form-control" name="username" placeholder="用户名">
            </div>
            <div class="mb-3">
                <label>邮箱</label>
                <input type="email" class="form-control" name="email" placeholder="邮箱">
            </div>
            <div class="mb-3">
                <label>验证码</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="验证码"
                           aria-label="Recipient's username" aria-describedby="button-addon2">
                    <button class="btn btn-outline-secondary" type="button">获取验证码</button>
                </div>
            </div>
            <div class="mb-3">
                <label>密码</label>
                <input type="password" class="form-control" name="password" placeholder="密码">
            </div>
            <div class="mb-3">
                <button class="btn btn-primary w-100">注册</button>
            </div>
        </form>
    </div>
</main>

</body>
</html>
```

![1731852015012](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731852015012.png)

验证码这个重要
![1731852067965](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731852067965.png)

### 7.发送验证码设置

- setting配置文件

```python
#邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 587
EMAIL_HOST_USER = '2494346096@qq.com'  # 发送邮件的邮箱帐号
EMAIL_HOST_PASSWORD = 'xntdswyfsqfpdihb'  # 授权码,各邮箱的设置中启用smtp服务时获取
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  #收件人显示发件人的邮箱
EMAIL_USE_SSL = True   # 使用ssl
# EMAIL_USE_TLS = False # 使用tls
# EMAIL_USE_SSL 和 EMAIL_USE_TLS 是互斥的，即只能有一个为 True
```

EMAIL_HOST_PASSWORD = 'xntdswyfsqfpdihb'  # 授权码,各邮箱的设置中启用smtp服务时获取，这是在开启邮箱发送服务会有

- 在view.py编写函数

```python
def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '必须传递邮箱'})
    # 生成验证码（取随机的4位阿拉伯数字）
    captcha = "".join(random.sample(string.digits, 4))
    try:
        send_mail(
            subject='博客之旅注册验证码',
            message=f"您的验证码是: {captcha}",
            from_email=None,  # 请在 settings.py 中设置 DEFAULT_FROM_EMAIL 或直接在此处指定
            recipient_list=[email]
        )
        return JsonResponse({"code": 200, "message": "邮箱验证码发送成功！"})
    except Exception as e:
        return JsonResponse({"code": 500, "message": "发送失败", "error": str(e)})
```

- 在urls.py里面配置路由

```python
from django.urls import path
from . import views

app_name = 'bkauth'
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email'),
]
```

### 8.数据库配置，验证码存储

- 配置文件setting里面加入MySQL数据库配置

```python
#数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

- 在bkauth里的modle.py文件里创建存储邮箱的表

```python
from django.db import models

# Create your models here.
class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
```

- 在原来的函数里加一行代码存储到数据库

![1731916538593](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1731916538593.png)

### 9.获取验证码按钮倒计时

