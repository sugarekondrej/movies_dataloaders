from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(
        Director,
        related_name='movies',
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return self.title