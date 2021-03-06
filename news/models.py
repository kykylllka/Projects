from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='photos')