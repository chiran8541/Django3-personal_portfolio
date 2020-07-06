from django.shortcuts import render,get_object_or_404
from .models import blog

def all_blogs(request):
    blogs = blog.objects.all()

    return render(request,'blog/all_blog.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_id= get_object_or_404(blog, pk =blog_id)
    return render(request,'blog/detail.html',{'blog':blog_id})


    

