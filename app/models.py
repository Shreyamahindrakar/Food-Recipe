
from django.db import models

# Create your models here.

CATEGORY_CHOICE=(
    ('VR','Vegetarian recipes'),
    ('NVR','NonVegetarian recipes'),
    ('O','Other'),
    
)
class FoodRecipe(models.Model):
    recipe_name = models.CharField(max_length=122,null=True,blank=True)
    ingredient = models.TextField(null=True,blank=True,help_text="Ingredient used for making recipe")
    description = models.TextField(null=True,blank=True,help_text="Description used for making recipe")
    category = models.CharField(max_length=22,choices=CATEGORY_CHOICE)
    recipe_image = models.ImageField(upload_to='recipeimg')
    
    def __str__(self):
        return str(self.id)

