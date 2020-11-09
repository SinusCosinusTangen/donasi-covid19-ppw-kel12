from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name
