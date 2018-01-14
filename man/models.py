from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.title


class Usage(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.title
