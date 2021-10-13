from django.db import models

# Create your models here.

STATUS = (
    ('Current', 'Current'),
    ('Completed', 'Completed'),
    ('Deleted', 'Deleted'),
)

class Current(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True)
