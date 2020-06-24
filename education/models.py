from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Religion(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=100)
    religion = models.ForeignKey(Religion, related_name='topic', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Subtopic(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField('contents')

    topic = models.ForeignKey(Topic, related_name='subtopic', on_delete=models.CASCADE)
    #image = models.ForeignKey(Images, related_name='subtopic_image', on_delete=models.CASCADE)
    def __str__(self):
        return self.title






