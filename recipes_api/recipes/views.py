from rest_framework.decorators import api_view
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import status

CONVERSION_RATES = {
    "grams": {"pounds": 0.0022},
    "ml": {"ounces": 0.0338},
    "pounds": {"grams": 453.6},
    "ounces": {"ml": 29.5735}
}

@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_recipe_ingredients(request, title):
    servings = int(request.query_params.get('servings', 1))
    try:
        recipe = Recipe.objects.get(title=title)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    ingredients = recipe.ingredients.all()
    adjusted_ingredients = [
        {
            "name": ing.name,
            "quantity": ing.quantity * servings,
            "unit": ing.unit
        }
        for ing in ingredients
    ]
    return Response(adjusted_ingredients)

@api_view(['GET'])
def convert_units(request, title, servings=1, target_unit=None):
    try:
        recipe = Recipe.objects.get(title=title)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    ingredients = recipe.ingredients.all()
    converted_ingredients = []
    
    for ing in ingredients:
        quantity = ing.quantity * servings
        if target_unit and target_unit in CONVERSION_RATES.get(ing.unit, {}):
            quantity *= CONVERSION_RATES[ing.unit][target_unit]
            unit = target_unit
        else:
            unit = ing.unit

        converted_ingredients.append({"name": ing.name, "quantity": quantity, "unit": unit})

    return Response(converted_ingredients)