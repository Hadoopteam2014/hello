from django.db import models

class UserProfile(models.Model):
       userid=models.CharField(max_length=100,primary_key=True)
       gender=models.CharField(max_length=100)
       email=models.CharField(max_length=100)
       name=models.CharField(max_length=100)
       familyname=models.CharField(max_length=100)
       givenname=models.CharField(max_length=100)
       agerange=models.IntegerField(max_length=100)
       language=models.CharField(max_length=100)
       circledByCount=models.IntegerField()
