from rest_framework import serializers
from leads.models import User_Account
from leads.models import Summoner

class UserAccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Account
    field = '__all__'

class SummonerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Summoner
    field = '__all__'
