from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

from .models import Frame, Strip, Deck, Tag


def portfolio_index(request):
    strips = Strip.objects.all()
    context = {'strips': strips}
    return render(request, 'portfolio/portfolio.html', context)


def strip_page(request, strip_title):
    strip = get_object_or_404(Strip, strip_title=strip_title)
    context = {'strip': strip}
    return render(request, 'portfolio/strip_page.html', context)

# def table_of_contents(request):
#     sections = Section.objects.all()
#     context = {'sections': sections}
#     return render(request, 'portfolio/portfolio.html', context)


# def section_page(request, section_title):
#     section = get_object_or_404(Section, section_title=section_title)
#     projects = Project.objects.all()
#     pieces = Piece.objects.all()
#     context = {'section': section,
#                'projects': projects,
#                'pieces': pieces}
#     return render(request, 'portfolio/strip_page.html', context)
