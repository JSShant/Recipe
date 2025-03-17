from django.urls import path
from .views import get_all_recipes

urlpatterns = [
  path('recipes/', get_all_recipes)
]
