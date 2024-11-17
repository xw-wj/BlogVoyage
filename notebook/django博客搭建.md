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
