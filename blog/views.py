from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect

#from datetime import datetime

from blog.models import *
from blog.forms import *
import datetime

#分页
def paginate(request, datas):
    paginator = Paginator(datas, 5)  # 创建Paginator
    page = request.GET.get('p')  # 获取当前页码
    try:
        contacts = paginator.page(page)  # 获取当前页码包含的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)  # 若不是整数，跳转到第一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)  # 如果超过最后一页，到最后一页
    return contacts, paginator

# Create your views here.
#主页
def main_page(request):
    articles = Article.objects.all().order_by('-create_time')
    # 标签搜索
    c = request.GET.get('c', '')
    if c:
        articles = articles.filter(category=c, ).order_by('-create_time')
    contacts, paginator = paginate(request, articles)
    return render(request, 'home.html', {'articles': contacts, 'pages': paginator})

#搜索
def blog_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s:
        articles = Article.objects.filter(Q(title__icontains=s)|Q(content__icontains=s)).order_by('-create_time')
    # 分页
    contacts, paginator = paginate(request, articles)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

#按月归档
def blog_monthly(request, year, month):
    blog_per_month = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    contacts, paginator = paginate(request, blog_per_month)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

#博客列表页
def blog_list(request):
    articles = Article.objects.all().order_by('-create_time')
    contacts, paginator = paginate(request, articles)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

#正文页
def blog_page(request, blogpost_id):
    article = get_object_or_404(Article, pk=blogpost_id)
    pre_article = Article.objects.filter(create_time__gt=article.create_time).first()   # greater_than
    next_article = Article.objects.filter(create_time__lt=article.create_time).last()    # less_than
    return render(request, 'blog.html', {'article': article, 'previous': pre_article, 'next': next_article})

#关于我
def about_me(request):
    userinfo = UserProfile.objects.get(pk=1)  # 站长资料 primary key
    return render(request, 'about.html', {'user': userinfo})
