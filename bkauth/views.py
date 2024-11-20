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


def login(request):
    return render(request, 'login.html')


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


def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '必须传递邮箱'})
    # 生成验证码（取随机的4位阿拉伯数字）
    captcha = "".join(random.sample(string.digits, 4))
    # 存储数据库
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail('博客之旅注册验证码', message=f"您的验证码是:{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "邮箱验证码发送成功！"})
