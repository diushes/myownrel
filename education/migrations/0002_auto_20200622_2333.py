# Generated by Django 3.0.7 on 2020-06-22 17:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
