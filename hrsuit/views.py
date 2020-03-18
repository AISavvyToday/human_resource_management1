from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Post

def home_view(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request,'home.html', context)

def blog_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/blog.html', context)


