from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

from .models import Section, Project


def index(request):
    table_of_contents = Section.objects.all()
    context = {'full_table': table_of_contents}
    return render(request, 'portfolio/index.html', context)


def section(request, section_id):
    title = get_object_or_404(Section, pk=section_id)
    context = {'section': title}
    return render(request, 'portfolio/section.html', context)
