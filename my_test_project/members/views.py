from typing import Any
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Member
from django.shortcuts import render


def members(request: HttpRequest):
    template = loader.get_template("all_members.html")
    my_members = Member.objects.all()
    context = {
        "members": my_members,
    }
    return HttpResponse(template.render(context, request))


def details(request: HttpRequest, member_id: int):
    template = loader.get_template("details.html")
    member = Member.objects.get(id=member_id)
    context = {
        "member": member,
    }
    return HttpResponse(template.render(context, request))


def main(request: HttpRequest):
    # template = loader.get_template("main_index.html")
    return render(request, template_name="main_index.html")


def my_name(name: str):
    if name:
        return name.upper()
    return "Gaurav Abhiman Mahajan"


def sample(request: HttpRequest):
    name1 = my_name("Some Random Person")
    context: dict[str, Any] = {"somerandom": 83, "name": name1}
    return render(request, "pages/sample.html", context)
