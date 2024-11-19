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
