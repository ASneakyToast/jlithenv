from django.db import models

# Create your models here.


class Section(models.Model):
    section_title = models.CharField(max_length=250)

    def __str__(self):
        return self.section_title


class Project(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    model_title = models.CharField(max_length=250)

    def __str__(self):
        return self.model_title
