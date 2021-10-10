<<<<<<< HEAD
"""import user model timezone"""
=======
"""ku polls model"""
>>>>>>> iteration2
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
<<<<<<< HEAD
    """set a question"""
=======
    """check publish"""
>>>>>>> iteration2

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date', null=True)

    def __str__(self):
        """return str"""
        return self.question_text

    def was_published_recently(self):
        """check is it public"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """if pubtime is not over yet,return True"""
        now = timezone.now()
        return self.pub_date <= now

    def can_vote(self):
        """if voting is currently allowed for this question,return true """
        now = timezone.now()
        return (self.pub_date <= now) and (now < self.end_date)


class Choice(models.Model):
<<<<<<< HEAD
    """set a choice"""
=======
    """choice model"""
>>>>>>> iteration2

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """return str"""
        return self.choice_text


class Vote(models.Model):
    """Vote Model.
    Args:
    models : Vote details (question, choice, user)
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True,
                             blank=True, on_delete=models.CASCADE)
