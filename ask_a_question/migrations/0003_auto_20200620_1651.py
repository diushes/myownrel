# Generated by Django 3.0.7 on 2020-06-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_a_question', '0002_auto_20200620_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
