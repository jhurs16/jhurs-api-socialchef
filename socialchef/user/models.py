from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# - favorite cuisine
# 	- favorite appliances
# 	- favorite spices
# 	- recipes submitted
	# - post submitted
class Profile(models.Model):
    """ For User Profile """
    STATUS = [
        ("A", "Active"),
        ("I", "InActive"),
        ("F", "Featured Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, blank=True, null=True)
    favorite_cuisine = models.CharField(max_length=500, blank=True, null=True)
    favorite_spices = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/',default="profiles/user-default.png")
    status = models.CharField(max_length=1, choices=STATUS, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    # for checking if the user image is deleted 
    @property
    def imageURL(self):
        try:
            url = self.profile_image.url 
        except:
            url = '/images/profiles/user-default.png'
        return url