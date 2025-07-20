from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Blog


# Create your views here.
def all_blogs(request: HttpRequest):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blogs/home.html", context=context)


def blog_details(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {"blog": blog}
    return render(request, template_name="blogs/blog_detail.html", context=context)
