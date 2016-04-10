from django.shortcuts import render
from .models import Projects


def list(request):
    projects = Projects.objects.all()
    return render(request, 'news/list.html', {'projects': projects})


