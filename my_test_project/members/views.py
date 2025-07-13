from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Member

def members(request: HttpRequest):
    template = loader.get_template('all_members.html')
    my_members = Member.objects.all()
    context = {
        'members': my_members,
    }
    return HttpResponse(template.render(context, request))

def details(request: HttpRequest, member_id: int):
    template = loader.get_template('details.html')
    member = Member.objects.get(id=member_id)
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))


def main(request: HttpRequest):
    template = loader.get_template('main_index.html')
    return HttpResponse(template.render())