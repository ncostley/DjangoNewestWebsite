from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(default = "", unique = True, max_length = 30)
    email = models.EmailField(unique = True, max_length = 30)
    review = models.TextField(default = "")
    priority = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name[0:30]
    
DISH_CHOICES = {
    "VEGAN": "Vegan",
    "VEG": "Vegetarian",
    "PESC": "Pescatarian",
    "MEAT": "Meat Eaters"
}

class Recipe(models.Model):
    dish_name = models.CharField(default = "", unique = True, max_length = 30)
    recipe = models.TextField(default = "")
    type = models.CharField(default = "", max_length=5, choices=DISH_CHOICES)
    #picture = models.ImageField(null=True, blank=True, upload_to="images/", default = False)

    def __str__(self):
        return self.dish_name