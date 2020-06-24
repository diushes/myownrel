from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=255, blank=False)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    faq = models.BooleanField(default=False)

    def __str__(self):
        return self.question