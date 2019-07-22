from django.db import models



class Section(models.Model):
    section_title = models.CharField(max_length=250)
    section_color = models.CharField(max_length=250, default='#656C6C')
    section_description = models.CharField(max_length=250, default='No description provided.')

    def __str__(self):
        return self.section_title


class Project(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    model_title = models.CharField(max_length=250)

    def __str__(self):
        return self.model_title


class Piece(models.Model):
    piece_title = models.CharField(max_length=250)
    date_created = models.DateTimeField('date created')
    description_quick = models.CharField(max_length=250)
    image_cover = models.ImageField(upload_to='images/pieces/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.piece_title

# class Example(models.Model):
#     author = Author.objects.get(name='Rod Dhl')
#     get_object_or_404(author.book_set, title='Matilda')
#
#     def __str__(self):
#         return self.model_title

# Shell Example
# from portfolio import Section
# section.objects.all() #Show all sections
# varName = section.objects.get(id = 1) #Get object and assign to var
# varName.attName = "strings"
# varName.save()
