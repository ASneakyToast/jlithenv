from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

from .models import Section, Project


def table_of_contents(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'portfolio/portfolio.html', context)


def section_page(request, section_title):
    title = get_object_or_404(Section, section_title=section_title)
    context = {'title': title}
    return render(request, 'portfolio/section_page.html', context)
