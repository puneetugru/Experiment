from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

#Adding below lines
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name