from django.urls import path
from .views import get_all_recipes, get_recipe_ingredients, convert_units

urlpatterns = [
  path('recipes/', get_all_recipes),
  path('recipes/<str:title>/ingredients/', get_recipe_ingredients),
  path('recipes/<str:title>/ingredients/<int:servings>/<str:target_unit>/', convert_units),
]
