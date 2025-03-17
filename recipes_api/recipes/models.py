from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"

