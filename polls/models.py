import datetime

from django.db import models

class Question(models.Model):
    text=models.CharField(max_length=100)
    pub_datetime=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.text} (id={self.id})'

class Choice(models.Model):
    text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.text}-{self.text}'

    class Meta:
        ordering=["-votes"]
# Create your models here.
