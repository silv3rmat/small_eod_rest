from django.db import models

# Create your models here.


class File(models.Model):
    path = models.FilePathField()
    name = models.CharField(max_length=100)


class FileSigner(models.Model):
    class Method(models.TextChoices):
        POST = 'POST', 'POST'
        PUT = 'PUT', 'PUT'

    name = models.CharField(max_length=100)
    method = models.CharField(choices=Method.choices, default=Method.POST, max_length=4)
    url = models.URLField()
    path = models.FilePathField()

