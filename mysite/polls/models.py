import datetime
from django.db import models
from django.utils import timezone


class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date Published')

    def __str__(self):
        return self.question_text
    def _was_published_recently(self):
        return self.pub_date >=timezone.now() -datetime.timedelta(days=1)



class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
