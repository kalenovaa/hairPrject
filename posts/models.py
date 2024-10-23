from tkinter import image_types

from django.db import models


class Login(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rate = models.IntegerField(default=0)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title