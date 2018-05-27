from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.http import HttpResponseRedirect

#from datetime import datetime

from blog.models import *
from blog.forms import SearchForm

# Create your views here.
def main_page(request):
    articles = Article.objects.all().order_by('-create_time')
    # 标签搜索
    c = request.GET.get('c', '')
    if c:
        articles = articles.filter(category=c, ).order_by('-create_time')
    #关键词搜索
    s = ''
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            s = request.GET.get('s')
    if s:
        articles = articles.filter(Q(title__contains=s)|Q(content__contains=s)).order_by('-create_time')
    # 分页
    paginator = Paginator(articles, 2)  # 创建Paginator
    page = request.GET.get('p') # 获取当前页码
    try:
        contacts = paginator.page(page) # 获取当前页码包含的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)    # 若不是整数，跳转到第一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)  # 如果超过最后一页，到最后一页
    return render(request, 'home.html', {'articles': contacts, 'pages': paginator})


def blog_page(request, blogpost_id):
    article = Article.objects.get(id=blogpost_id)
    return render(request, 'blog.html', {'article': article})


def edit_page(request, blogpost_id):
    if str(blogpost_id) == '0':
        return render(request, 'edit.html')
    else:
        article = Article.objects.get(id=blogpost_id)
        return render(request, 'edit.html', {'article': article})


def post_blog(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    #category = request.POST.get('category', 'CATEGORY')
    blogpost_id = request.POST.get('blogpost_id', '0')
    if blogpost_id == '0':  # 编辑新博客
        Article.objects.create(title=title, content=content, category_id=1)
        # new_blog.save()
        articles = Article.objects.order_by('-create_time')
        return render(request, 'home.html', {'articles': articles})
        # return HttpResponseRedirect('')
    else:
        new_blog = Article.objects.get(id=blogpost_id)
        new_blog.title = title
        new_blog.content = content
        new_blog.save()
        articles = Article.objects.order_by('-create_time')
        return render(request, 'home.html', {'articles': articles})

def blog_tags(request):
    categories = Category.objects.all().order_by('sort_id')
    return render(request, 'tags.html', {'categories': categories})
