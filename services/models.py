from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title
