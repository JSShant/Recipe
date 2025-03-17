from django.urls import path
from .views import get_all_recipes, get_recipe_ingredients, convert_units

urlpatterns = [
  path('recipes/', get_all_recipes),
  path('recipes/<int:recipe_id>/ingredients/<int:servings>/', get_recipe_ingredients),
  path('recipes/<int:recipe_id>/ingredients/<int:servings>/<str:target_unit>/', convert_units),
]
