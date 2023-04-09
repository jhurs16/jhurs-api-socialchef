from django.db import models
# from django.contrib.auth.models import User
from user.models import Profile

# Create your models here.
class Article(models.Model):
    STATUS = [
        ("A", "Active"),
        ("I", "InActive"),
        ("L", "Latest"),
    ]
    name = models.CharField(null=True, max_length=200, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    content = models.TextField(null=True, blank=True)
    stats = models.CharField(max_length=1, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name