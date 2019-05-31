from django.shortcuts import render

from .models import Section, Project


def index(request):
    full_table = Section.objects.all()
    context = {'full_table': full_table}
    return render(request, 'portfolio/index.html', context)


def section(request):
    table_of_projects = Project.objects.all()
    context = {'table_of_projects': table_of_projects}
    return render(request, 'portfolio/section.html', context)
