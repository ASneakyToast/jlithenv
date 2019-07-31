from django.contrib import admin

from .models import Tag, Deck, Strip, Frame

admin.site.register(Tag)
admin.site.register(Deck)
admin.site.register(Frame)


# class FrameInline(admin.TabularInline):
#     model = Frame
#     extra = 3


class StripAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['strip_title', 'strip_altText']}),
        ('Frames', {'fields': ['strip_frames']}),
    ]
    # inlines = [FrameInline]
    list_display = ('strip_title', 'strip_altText')
    filter_horizontal = ('strip_frames',)


admin.site.register(Strip, StripAdmin)


# 'TODO Come back to https://docs.djangoproject.com/en/2.2/intro/tutorial07/ and learn about sorting/filtering by date'
