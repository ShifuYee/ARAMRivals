from leads.models import User_Account
from leads.models import Summoner
from leads.serializers import UserAccountSerializer
from leads.serializers import SummonerSerializer
from rest_framework import generics # generic API views

# RetrieveUpdateDestroy - Used for read-write-delete endpoints to represent a single model instance

class UserAccountRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User_Account.objects.all()
  serializer_class = UserAccountSerializer

class SummonerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Summoner.objects.all()
  serializer_class = SummonerSerializer
