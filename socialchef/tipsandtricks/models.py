from django.db import models
# Create your models here.

class TipsandTrick(models.Model):
    name = models.CharField(null=True, max_length=200, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
