from django.db import models

class User_Account(models.Model):
  username = models.CharField(max_length=20)
  username_lower = models.CharField(max_length=20)

class User_Session(models.Model):
  user_id = models.BigIntegerField()
  creation_time = models.BigIntegerField()

class Summoner(models.Model):
  account_id = models.BigIntegerField()
  summoner_id = models.BigIntegerField()
  summoner_name = models.CharField(max_length=20)
  damage_dealt = models.BigIntegerField()
  damage_taken = models.BigIntegerField()
  damage_dealt_to_turrets = models.BigIntegerField()
