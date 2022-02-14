from django.shortcuts import render
from .models import Blogpost
from math import ceil
# Create your views here.


def index(request):
    blogpost = Blogpost.objects.all()
    params = {'blogpost': blogpost}
    return render(request, 'blog/index.html', params)


def blogPost(request, bid):
    blog = Blogpost.objects.filter(post_id=bid)[0]
    return render(request, 'blog/blogpost.html', {'blogpost': blog})
