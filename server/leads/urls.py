from django.urls import path
from . import views

urlpatterns = [
  path('api/userAccount/', views.UserAccountRetrieveUpdateDestroy.as_view()),
  path('api/Summoner/', views.SummonerRetrieveUpdateDestroy.as_view()),
]
