from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-pub_date') #쿼리셋 = 모델을 오브젝트의 목록을 가져온다고 생각, 메소드
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.memo = request.GET['memo']
    blog.cata = request.GET['cata']
    blog.save() #쿼리 메소드
    return redirect('home')

def edit(request, blog_id): # CRUD의 U인데 edit 수정할 게시글들을 가져오는 부분
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog': blog })

def update(request, blog_id): # CRUD U 수정을 하구 다시 저장하는 부분
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.memo = request.GET['memo']
    blog.cata = request.GET['cata']
    blog.save() #쿼리 메소드
    return redirect('home')

def delete(request, blog_id): # CRUD D 게시글을 삭제하는 부분
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete() #쿼리 메소드
    return redirect('home')