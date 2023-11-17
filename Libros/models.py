from django.db import models

# Create your models here.
class Libros(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField()
    sinopsis = models.TextField()
    created_at=models.TimeField()
    update_at=models.TimeField()

    def __str__(self):
      return self.title