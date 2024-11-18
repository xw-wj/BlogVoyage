import random
import string

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .models import CaptchaModel


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


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




