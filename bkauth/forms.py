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
