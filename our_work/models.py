from django.db import models


class OurWork(models.Model):
    """A representation of the work that we have done for customers"""
    title = models.CharField(max_length=200)
    about_site = models.TextField()
    imageURL = models.CharField(max_length=300)

    def __str__(self):
        return self.title
