from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=150, blank=False)
    level = models.PositiveIntegerField(default=1)
    passed_the_test = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def questions_count(self):
        return self.questions.all().count()


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    answer = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.question


class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')
    version = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.version