from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    ('Current', 'Current'),
    ('Completed', 'Completed'),
    ('Deleted', 'Deleted'),
)

class Current(models.Model):
    task = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True)


    class Meta:
        verbose_name_plural = "Current"


    def __str__(self):
        return self.task

class Completed(models.Model):
    task = models.ForeignKey(Current, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Completed"

    def __str__(self):
        return f'{self.task} was completed by {self.username}'


