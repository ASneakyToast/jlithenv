# Generated by Django 2.2.1 on 2019-06-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_section_section_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_title', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('description_quick', models.CharField(max_length=250)),
                ('image_cover', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='images/frames/')),
            ],
        ),
    ]
