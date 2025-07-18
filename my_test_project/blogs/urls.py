from django.urls import path
from .views import all_blogs

urlpatterns = [path("blogs/", all_blogs, name="blogs")]
