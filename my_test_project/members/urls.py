from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.AboutPage.as_view(), name="about"),
    path("about/details/<int:member_id>/", views.details, name="details"),
    path("", views.main, name="main"),
    path("sample/", views.sample, name="sample"),
]
