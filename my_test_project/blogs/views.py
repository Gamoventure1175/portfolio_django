from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy


# Create your views here.
# def all_blogs(request: HttpRequest):
#     blogs = Blog.objects.all()
#     context = {"blogs": blogs}
#     return render(request, "blogs/home.html", context=context)

# def blog_details(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     context = {"blog": blog}
#     return render(request, template_name="blogs/blog_detail.html", context=context)


# Switching to Class Based Views
class BlogsListView(ListView):
    template_name = "blogs/home.html"
    model = Blog


class BlogDetailView(DetailView):
    template_name = "blogs/blog_detail.html"
    model = Blog


class BlogCreateView(CreateView):
    template_name = "blogs/blog_new.html"
    model = Blog
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    template_name = "blogs/blog_update.html"
    model = Blog
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    template_name = "blogs/blog_delete.html"
    model = Blog
    success_url = reverse_lazy("blogs")
