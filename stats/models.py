from django.db import models

class Problems(models.Model):
    issue   = models.CharField(max_length=255)
    figure  = models.IntegerField()

    def __str__(self):
        return self.issue

