from django.urls import path
from .views import get_stats

app_name = 'stats'

urlpatterns = [
    path('', get_stats, name='stats')
]