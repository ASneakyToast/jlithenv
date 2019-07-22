from django.contrib import admin

from .models import Tag, Deck, Strip, Frame

admin.site.register(Tag)
admin.site.register(Deck)
admin.site.register(Strip)
admin.site.register(Frame)
