from django.db import models
from django.contrib.auth.models import User
from user.models import Profile
# Create your models here.
class Recipe(models.Model):
    DIFFICULTY = [
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
    ]
    STATUS = [
        ("A", "Active"),
        ("I", "InActive"),
        ("L", "Latest"),
        ("R", "Recipe of the Day")
    ]
    name = models.CharField(null=True, max_length=200, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    cooking_time = models.CharField(max_length=200, null=True, blank=True)
    difficulty_level = models.CharField(max_length=1, choices=DIFFICULTY)
    serves = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('RecipeCategory', on_delete=models.CASCADE, related_name="recipe_cat")
    ingredients = models.TextField(null=True, blank=True)
    procedure = models.TextField(null=True, blank=True)
    stats = models.CharField(max_length=1, choices=STATUS)
    likes = models.ManyToManyField(Profile, related_name="recipe_likes")
    posted_by = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.CASCADE,related_name="recipe_posted")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    name = models.CharField(null=True, max_length=200, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class NutritionFact(models.Model):
    name = models.CharField(null=True, max_length=200, blank=True)
    value = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="nutrition_fact"
    )
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe.name
    
class Comment(models.Model):
    content = models.TextField(null=True, blank=True)
    comment_by = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comment"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe.name