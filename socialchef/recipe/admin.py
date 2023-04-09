from django.contrib import admin

# Register your models here.
from .models import (
    Recipe,
    RecipeCategory,
    NutritionFact,
    Comment
)

class NutritionFactInline( admin.TabularInline):
    model = NutritionFact
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [NutritionFactInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory)
admin.site.register(Comment)