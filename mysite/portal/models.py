from django.db import models

# Create your models here.
class Job(models.Model):
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    package = models.FloatField()

    def __str__(self):
        return self.role
