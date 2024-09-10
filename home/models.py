from django.db import models

# Create your models here.
class Disease(models.Model):
    plant_name = models.CharField(max_length=255)  # Add this line
    name = models.CharField(max_length=100, unique=True)
    symptoms = models.TextField()
    cure = models.TextField()
    causes = models.TextField()
    prevention = models.TextField()
    image = models.ImageField(upload_to='disease_images/')
    Fertilizer_name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)  # e.g., organic, chemical, etc.
    usage_instructions = models.TextField()  # How to apply the fertilizer
    composition = models.TextField()  # Description of the nutrients and compounds
    Fertilizer_image = models.ImageField(upload_to='disease_images/')


    def __str__(self):
        return self.name