from typing import Any
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import TemplateView
from .models import Member
from django.shortcuts import render


class AboutPage(TemplateView):
    """About page - class based view"""

    template_name = "pages/about.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        all_members = Member.objects.all()
        context["members"] = all_members
        return context


def details(request: HttpRequest, member_id: int):
    template = loader.get_template("details.html")
    member = Member.objects.get(id=member_id)
    context = {
        "member": member,
    }
    return HttpResponse(template.render(context, request))


def main(request: HttpRequest):
    # template = loader.get_template("main_index.html")
    my_list_of_things = [
        "Enterpreneurship",
        "System Architecture",
        "Network Integration",
        "AI Infrastructure",
    ]

    context = {"what_we_do": my_list_of_things}
    return render(request, template_name="main_index.html", context=context)


def my_name(name: str):
    if name:
        return name.upper()
    return "Gaurav Abhiman Mahajan"


def sample(request: HttpRequest):
    name1 = my_name("Some Random Person")
    context: dict[str, Any] = {"somerandom": 83, "name": name1}
    return render(request, "pages/sample.html", context)
