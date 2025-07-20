from django.urls import path
from .views import all_blogs, blog_details

urlpatterns = [
    path("blogs/", all_blogs, name="blogs"),
    path("blogs/<int:pk>/", blog_details, name="blog_detail"),
]
