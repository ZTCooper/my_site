from django.shortcuts import render, redirect
from django.contrib import auth     #避免login冲突，引用到auth层
from django.urls import reverse


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('blog:main_page'))
    # 获取链接以重定向，如获取失败跳转至 blog:main_page（reverse反向解析url）
    if user is not None:
        #验证通过
        auth.login(request, user)
        return redirect(referer)    #重定向到之前页面
    else:
        #验证不通过
        return render(request, 'error.html', {'message':'用户名或密码不正确'})


