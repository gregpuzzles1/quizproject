# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

now = timezone.now()

naive_datetime = datetime.datetime(2025, 4, 14, 16, 45, 6, 367439)
aware_datetime = timezone.make_aware(naive_datetime, timezone.get_current_timezone())



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)
