# Generated by Django 3.0.7 on 2020-06-22 18:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200622_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
