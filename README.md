# Recipe List API

Python based API using Django to return a list of recipes.

## Setup Instructions
### 1. Adding Recipes to the Database
By default, one recipe exists in the database. To add more, follow these steps:

  **1. Open the Django Shell:**
     
     
     python manage.py shell
     
  **2. Run the following commands to create a new recipe and its ingredients:**

     
     from recipes.models import Recipe, Ingredient

     spaghetti = Recipe.objects.create(title="Spaghetti")
     Ingredient.objects.create(recipe=spaghetti, name="Pasta", quantity=500, unit="grams")
     Ingredient.objects.create(recipe=spaghetti, name="Tomato Sauce", quantity=300, unit="ml")
     Ingredient.objects.create(recipe=spaghetti, name="Ground Beef", quantity=250, unit="grams")
     
  . Modify the title, name, quantity, and unit values as needed to add different recipes.
  
  . Add multiple recipes by repeating the process.

  **3. Exit the shell after adding recipes:**

     
     exit()
     

### 2. Running the Server
**Start the Django development server:**

  ```
  python manage.py runserver
  ```
  

**To view all recipes visit:**

http://127.0.0.1:8000/api/recipes/

**To view a specific recipe vist:**

http://127.0.0.1:8000/api/recipes/{RecipeTitle}/ingredients/

**To view a specific recipe and amounts needed for multiple servings visit:**

http://127.0.0.1:8000/api/recipes/{RecipeTitle}/ingredients/?servings={servings}

**To Convert ml to ounces, or grams to pounds and vice versa visit:**

http://127.0.0.1:8000/api/recipes/{RecipeTitle}/ingredients/{conversionUnit}/

**How to Use the API**
. Replace {RecipeTitle} with the title of the recipe you want to retrieve (e.g., Spaghetti).

. Replace {servings} with the desired number of servings.

. Replace {conversionUnit} with the target unit (e.g., ounces or pounds).

## Example Usage
**View all recipes:**

 - http://127.0.0.1:8000/api/recipes/

**Get ingredients for Spaghetti:**

 - http://127.0.0.1:8000/api/recipes/Spaghetti/ingredients/

**Get ingredient amounts for 4 servings of Spaghetti:**

 - http://127.0.0.1:8000/api/recipes/Spaghetti/ingredients/?servings=4

**Convert Spaghetti ingredients to ounces:**

 - http://127.0.0.1:8000/api/recipes/Spaghetti/ingredients/ounces/



