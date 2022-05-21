from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=255, blank=False, null=False)
    optionOne = models.CharField(max_length=255, blank=False, null=False)
    optionTwo = models.CharField(max_length=255, blank=False, null=False)
    optionThree = models.CharField(max_length=255, blank=False, null=False)
    optionFour = models.CharField(max_length=255, blank=False, null=False)
    optionFive = models.CharField(max_length=255, blank=False, null=False)
    result = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question
