from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name="members"),
    path("members/details/<int:member_id>/", views.details, name="details"),
    path("", views.main, name="main"),
]
