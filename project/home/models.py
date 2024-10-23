from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    Author_Name = models.CharField(null=False, blank=False, max_length=250)
    description = models.CharField(null=False, blank=False, max_length=2000)

    def __str__(self):
        return self.Author_Name
    