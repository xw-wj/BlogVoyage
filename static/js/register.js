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