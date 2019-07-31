from django.db import models
import uuid

#
#   new data structure
# Tags (Art, Design, Vault, Current)
# Deck (Whole Project Series?) (everydays, thoughts, clusters)
# Strips (An entirety of a piece (all photos))
# Frame (a single part of a piece, a close up of a sculpture)
#

#     Abstracts     #


# class AbstractTags(models.Model):
#     tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     class Meta:
#         abstract = True


#     Frame Data     #
# ID = Unique identifier
# Title = "Gallery_Shot", if same name = "Gallery_Shot--2"
# Strips = Piece Name. "14_07_19"
# Decks = Project Series "Everydays"
# Tags = Art, Current
# Time = Date: date made, time: time posted
# Alt-Text Override =


class Frame(models.Model):
    frame_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frame_title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/frames/', default='pic_folder/None/no-img.jpg')
    # 'TODO Make a date created field here'

    def __str__(self):
        # 'TODO Use the title + date created fields to make a name like: 06_04_19-Gallery_Shot'
        return self.frame_title


#     Strips Data     #
# ID = Unique identifier
# Title = "14_07_19", can only be one title
# Alt-Text = Story/alt-text
# Tags = Art, Current
# Time-Span = start frame to end frame


class Strip(models.Model):
    strip_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strip_title = models.CharField(max_length=250)
    strip_altText = models.CharField(max_length=447)
    strip_frames = models.ManyToManyField(Frame)

    def __str__(self):
        return self.strip_title


#     Tags     #
# ID = Unique identifier
# Title = "Everydays", "Components"
# Decks = all decks related
# Strips = all strips related
# Frames = All frames related


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_name = models.CharField(max_length=250)

    def __str__(self):
        return self.tag_name

#     Deck Data     #
# ID
# Title
# Tags
# Strips
# Frames
# Time-Span = Start strip to end strip


class Deck(models.Model):
    deck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deck_title = models.CharField(max_length=250)
    deck_tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.deck_title


# Old Data things #
#
# class Section(models.Model):
#     section_title = models.CharField(max_length=250)
#     section_color = models.CharField(max_length=250, default='#656C6C')
#     section_description = models.CharField(max_length=250, default='No description provided.')
#
#     def __str__(self):
#         return self.section_title
#
#
# class Project(models.Model):
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#     model_title = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.model_title
#
#
# class Piece(models.Model):
#     piece_title = models.CharField(max_length=250)
#     date_created = models.DateTimeField('date created')
#     description_quick = models.CharField(max_length=250)
#     image_cover = models.ImageField(upload_to='images/frames/', default='pic_folder/None/no-img.jpg')
#
#     def __str__(self):
#         return self.piece_title

# class Example(models.Model):
#     author = Author.objects.get(name='Rod Dhl')
#     get_object_or_404(author.book_set, title='Matilda')
#
#     def __str__(self):
#         return self.model_title

# Shell Example
# python manage.py shell
# from portfolio.models import Section
# section.objects.all() #Show all sections
# varName = section.objects.get(id = 1) #Get object and assign to var
# varName.attName = "strings"
# varName.save()
