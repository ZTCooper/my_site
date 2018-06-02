from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from read_num.utils import read_increase
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from read_num.models import ReadNum
from blog.models import *
from blog.forms import *


#分页
def paginate(request, datas, nums):
    paginator = Paginator(datas, nums)  # 创建Paginator，每页nums条
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
    return render(request, 'home.html')

#搜索
def blog_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s:
        articles = Article.objects.filter(Q(title__icontains=s)|Q(content__icontains=s)).order_by('-create_time')
    # 分页
    contacts, paginator = paginate(request, articles, 5)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

def blah_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s:
        blahs = BlahBlah.objects.filter(Q(content__icontains=s)).order_by('-create_time')
    # 分页
    contacts, paginator = paginate(request, blahs, 10)
    return render(request, 'blah_list.html', {'blahs': contacts, 'pages': paginator})

#按月归档
def blog_monthly(request, year, month):
    blog_per_month = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    contacts, paginator = paginate(request, blog_per_month, 5)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

#博客列表页
def blog_list(request):
    articles = Article.objects.all().order_by('-create_time')
    #标签搜索
    t = request.GET.get('t', '')
    if t:
        articles = Article.objects.filter(tag__contains=t, ).order_by('-create_time')
        # 分类搜索
    c = request.GET.get('c', '')
    if c:
        articles = Article.objects.filter(category=c, ).order_by('-create_time')
    contacts, paginator = paginate(request, articles, 5)
    return render(request, 'list.html', {'articles': contacts, 'pages': paginator})

#正文页
def blog_page(request, blogpost_id):
    article = get_object_or_404(Article, pk=blogpost_id)

    read_cookies_key = read_increase(request, article)  # 阅读量+1

    pre_article = Article.objects.filter(create_time__gt=article.create_time).first()   # greater_than
    next_article = Article.objects.filter(create_time__lt=article.create_time).last()    # less_than

    response = render(request, 'blog.html', {'article': article, 'previous': pre_article, 'next': next_article})
    response.set_cookie(read_cookies_key, 'true', max_age=30)   # 阅读cookie标记，30s有效期
    return response

#关于我
def about_me(request):
    userinfo = UserProfile.objects.get(pk=1)  # 站长资料 primary key
    return render(request, 'about.html', {'user': userinfo})

#碎碎念列表页
def blah_list(request):
    blahs = BlahBlah.objects.all().order_by('-create_time')
    # 标签搜索
    t = request.GET.get('t', '')
    if t:
        blahs = BlahBlah.objects.filter(tag__contains=t, ).order_by('-create_time')
    contacts, paginator = paginate(request, blahs, 10)
    return render(request, 'blah_list.html', {'blahs': contacts, 'pages': paginator})

def blah_detail(request, blah_id):
    blah = get_object_or_404(BlahBlah, pk=blah_id)

    read_cookies_key = read_increase(request, blah)  # 阅读量+1

    pre_blah = BlahBlah.objects.filter(create_time__gt=blah.create_time).first()  # greater_than
    next_blah = BlahBlah.objects.filter(create_time__lt=blah.create_time).last()  # less_than

    response =  render(request, 'blah_detail.html', {'blah': blah, 'previous': pre_blah, 'next': next_blah})
    response.set_cookie(read_cookies_key, 'true', max_age=30)  # 阅读cookie标记，30s有效期
    return response