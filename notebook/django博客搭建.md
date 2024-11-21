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

- 下载jquery，并且在register.html 里面加个id

![1732019490868](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1732019490868.png)

- 在/static/js 里面创建个register.js,里面填写内容

```javascript
$(function() {
    $("#captcha-btn").click(function(event){
        let $this = $(this);
        let email = $("input[name='email']").val(); // 注意单引号和等号两边的引号要匹配
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/; // 简单的电子邮件正则表达式

        if(!email) {
            alert("请先输入邮箱地址！");
        } else if (!emailRegex.test(email)) {
            alert("邮箱地址格式不正确，请重新输入！");
        } else {
            // 邮箱地址有效，禁用按钮并开始倒计时
            $this.prop('disabled', true);
            $this.text("等待中..."); // 更新按钮文本

            let countdown = 60; // 设置倒计时时间，例如60秒
            let countdownElement = $("#captcha-btn");

            countdownElement.text(countdown + "秒后重新获取");

            var interval = setInterval(function(){
                countdown--; // 每次触发倒计时减1
                if(countdown < 0){
                    clearInterval(interval); // 倒计时结束，清除定时器
                    countdownElement.text("重新获取验证码"); // 重置按钮文本
                    countdownElement.prop('disabled', false); // 启用按钮
                } else {
                    countdownElement.text(countdown + "秒后重新获取"); // 更新按钮文本
                }
            }, 1000); // 每秒触发一次
        }
    })
});
```

### 10.完成获取验证码功能

修改static/js/register.js，修改加上ajax请求
```javascript
$(function() {
    $("#captcha-btn").click(function(event){
        let $this = $(this);
        let email = $("input[name='email']").val(); // 获取输入框中的邮箱地址
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/; // 简单的电子邮件正则表达式

        if (!email) {
            alert("请先输入邮箱地址！");
        } else if (!emailRegex.test(email)) {
            alert("邮箱地址格式不正确，请重新输入！");
        } else {
            // 邮箱地址有效，禁用按钮并开始倒计时
            $this.prop('disabled', true);
            $this.text("等待中..."); // 更新按钮文本

            // 发送 AJAX 请求到后端
            $.ajax({
                url: "/auth/captcha", // 对应的后端路由路径
                method: "GET", // 使用 GET 请求
                data: {
                    email: email // 将邮箱地址作为参数发送
                },
                success: function(response) {
                    if (response.code === 200) {
                        // 请求成功后的处理
                        alert(response.message);

                        // 开始倒计时
                        let countdown = 60; // 设置倒计时时间
                        let countdownElement = $("#captcha-btn");

                        countdownElement.text(countdown + "秒后重新获取");

                        var interval = setInterval(function() {
                            countdown--; // 每次触发倒计时减1
                            if (countdown < 0) {
                                clearInterval(interval); // 倒计时结束，清除定时器
                                countdownElement.text("重新获取验证码"); // 重置按钮文本
                                countdownElement.prop('disabled', false); // 启用按钮
                            } else {
                                countdownElement.text(countdown + "秒后重新获取"); // 更新按钮文本
                            }
                        }, 1000); // 每秒触发一次
                    } else {
                        // 其他错误处理
                        alert("发送验证码失败：" + response.message);
                        $this.prop('disabled', false);
                        $this.text("获取验证码");
                    }
                },
                error: function(xhr, status, error) {
                    // 请求失败后的处理
                    alert("验证码发送失败，请稍后重试！");
                    $this.prop('disabled', false);
                    $this.text("获取验证码");
                }
            });
        }
    });
});

```

### 11.完成注册功能

- 在bkauth下创建forms.py文件

```python
from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

# 获取用户模型，支持自定义用户模型的项目
User = get_user_model()


class RegisterForm(forms.Form):
    # 用户名字段，限制长度为 2-30，定义错误信息
    username = forms.CharField(
        max_length=30,
        min_length=2,
        error_messages={
            'required': '请传入用户名！',          # 当用户名字段为空时提示
            'min_length': '用户名至少2个字符！',   # 用户名少于 2 个字符时提示
            'max_length': '用户名最多30个字符！'    # 用户名超过 30 个字符时提示
        }
    )

    # 邮箱字段，使用 Django 内置的 EmailField 验证邮箱格式，定义错误信息
    email = forms.EmailField(
        error_messages={
            'required': '请传入邮箱！',         # 当邮箱字段为空时提示
            'invalid': '请传入一个正确邮箱！'     # 邮箱格式不正确时提示
        }
    )

    # 密码字段，限制长度为 6-30，使用 PasswordInput 控件隐藏输入，定义错误信息
    password = forms.CharField(
        max_length=30,
        min_length=6,
        widget=forms.PasswordInput,  # 使用密码输入控件
        error_messages={
            'required': '请传入密码！',          # 当密码字段为空时提示
            'min_length': '密码至少6个字符！',   # 密码少于 6 个字符时提示
            'max_length': '密码最多30个字符！'    # 密码超过 30 个字符时提示
        }
    )

    # 验证码字段，长度固定为 4 位数字或字符
    captcha = forms.CharField(
        max_length=4,
        min_length=4
    )

    # 自定义邮箱字段的验证逻辑
    def clean_email(self):
        # 获取表单中输入的邮箱
        email = self.cleaned_data.get('email')

        # 检查邮箱是否已经注册
        if User.objects.filter(email=email).exists():
            # 如果邮箱已存在，抛出验证错误
            raise forms.ValidationError('该邮箱已被注册！')

        # 如果邮箱未被注册，返回其值
        return email

    # 自定义验证码字段的验证逻辑
    def clean_captcha(self):
        # 获取表单中输入的验证码
        captcha = self.cleaned_data.get('captcha')

        # 获取表单中输入的邮箱
        email = self.cleaned_data.get('email')

        # 验证验证码是否与数据库中匹配
        if not CaptchaModel.objects.filter(email=email, captcha=captcha).first():
            # 如果验证码不匹配，抛出验证错误
            raise forms.ValidationError('验证码不正确！')

        # 如果验证码正确，返回其值
        return captcha
```

- 在view里面修改register函数

```python
import random
import string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('bkauth:login'))
        else:
            print(form.errors)
            # 重新跳转到登陆页面
            return  redirect(reverse('bkauth:register'))
```

- 给register.html里面加入{%csrf token%}写在form里面第一行

### 12.完成登录功能

- 在bkauth里的forms.py文件加入验证传来的登录信息操作

```python
class LoginForm(forms.Form):
    # 邮箱字段，使用 Django 内置的 EmailField 验证邮箱格式，定义错误信息
    email = forms.EmailField(
        error_messages={
            'required': '请传入邮箱！',  # 当邮箱字段为空时提示
            'invalid': '请传入一个正确邮箱！'  # 邮箱格式不正确时提示
        }
    )

    # 密码字段，限制长度为 6-30，使用 PasswordInput 控件隐藏输入，定义错误信息
    password = forms.CharField(
        max_length=30,
        min_length=6,
        widget=forms.PasswordInput,  # 使用密码输入控件
        error_messages={
            'required': '请传入密码！',  # 当密码字段为空时提示
            'min_length': '密码至少6个字符！',  # 密码少于 6 个字符时提示
            'max_length': '密码最多30个字符！'  # 密码超过 30 个字符时提示
        }
    )
    # 记住我
    remember = forms.IntegerField(required=False)
```

- 在view里面修改login函数

```python
import random
import string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, authenticate, login as auth_login

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                auth_login(request, user)
                # 判断用户是否需要记住我
                if not remember:
                    # 如果没有点击记住我，那么就要设置过期时间为0，及浏览器关闭后机会过期
                    request.session.set_expiry(0)
                # 如果点击了就什么也不做，就默认两周的过期时间
                return redirect('blog:index')
            else:
                # form.add_error(None, '无效的登录信息')  # 添加错误消息
                # return render(request, 'login.html', {'form': form})
                return redirect(reverse('bkauth:login'))
```

### 13.登录与非登录状态切换

- 在base里面把注册与登陆的按钮标签里面的button改成<a>标签

```html
<a href="{% url 'bkauth:login' %}" type="button" class="btn btn-outline-primary me-2">登录</a>
<a href="{% url 'bkauth:register' %}" type="button" class="btn btn-primary">注册</a>
```

- 去https://getbootstrap.com/docs/5.3/examples/headers/ 找带头像的导航页，右击导出outhtml

![1732170464324](D:\BaiduNetdiskDownload\BlogVoyage\notebook\images\1732170464324.png)

- 改成下面这样

```html
{% if user.is_authenticated %}
    <div class="flex-shrink-0 dropdown">
        <a href="#" class="d-block link-body-emphasis text-decoration-none dropdown-toggle"
           data-bs-toggle="dropdown" aria-expanded="false">
            <img src="{% static 'image/avatar.jpeg' %}" alt="mdo" width="32" height="32" class="rounded-circle">
        </a>
        <ul class="dropdown-menu text-small shadow">
            <li><a class="dropdown-item" href="#">退出登录</a></li>
        </ul>
    </div>
{% else %}
    <div class="text-end">
        <a href="{% url 'bkauth:login' %}" type="button" class="btn btn-outline-primary me-2">登录</a>
        <a href="{% url 'bkauth:register' %}" type="button" class="btn btn-primary">注册</a>
    </div>
{% endif %}
```

