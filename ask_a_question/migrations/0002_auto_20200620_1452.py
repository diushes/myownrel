# Generated by Django 3.0.7 on 2020-06-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_a_question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, default=True),
        ),
    ]
