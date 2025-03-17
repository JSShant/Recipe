from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from recipes.models import Recipe, Ingredient

class RecipeAPITests(TestCase):
    
    def setUp(self):
        self.client = APIClient()

        self.recipe = Recipe.objects.create(title="Spaghetti Bolognese")
        
        self.ingredient_1 = Ingredient.objects.create(
            name="Ground Beef", 
            quantity=1000, 
            unit="grams", 
            recipe=self.recipe
        )
        
        self.ingredient_2 = Ingredient.objects.create(
            name="Tomato Sauce", 
            quantity=500, 
            unit="ml", 
            recipe=self.recipe
        )
    
    def test_get_all_recipes(self):
        url = '/api/recipes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_ingredient_amounts_based_on_servings(self):
        servings = 2

        url = f'/api/recipes/{self.recipe.id}/ingredients/{servings}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for ingredient in response.data:
            if ingredient['name'] == 'Ground Beef':
                expected_quantity = self.ingredient_1.quantity * servings
                self.assertEqual(ingredient['quantity'], expected_quantity)
            elif ingredient['name'] == 'Tomato Sauce':
                expected_quantity = self.ingredient_2.quantity * servings
                self.assertEqual(ingredient['quantity'], expected_quantity)
    
    def test_ingredient_conversion_to_ounces(self):
        
        servings = 1
        url = f'/api/recipes/{self.recipe.id}/ingredients/{servings}/ounces/' 
        response = self.client.get(url)
        
        for ingredient in response.data:
            if ingredient['unit'] == "ml":
                expected_quantity = self.ingredient_1.quantity * 0.033814    
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data[1]['name'], 'Tomato Sauce')
                self.assertAlmostEqual(response.data[1]['quantity'], expected_quantity, places=2)
                self.assertEqual(response.data[1]['unit'], 'ounces')
                
        
