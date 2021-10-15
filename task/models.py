from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

STATUS = (
    ('Current', 'Current'),
    ('Completed', 'Completed'),
    ('Deleted', 'Deleted'),
)

class Current(models.Model):
    task = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS, null=True)


    class Meta:
        verbose_name_plural = "Current"


    def __str__(self):
        return self.task

class Completed(models.Model):
    task = models.ForeignKey(Current, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS, null=True)


    class Meta:
        verbose_name_plural = "Completed"

    def __str__(self):
        return f'{self.task} was completed by {self.username}'


class Deleted(models.Model):
    task = models.ForeignKey(Current, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS, null=True)

    class Meta:
        verbose_name_plural = "Deleted"

    def __str__(self):
        return f'{self.user} was deleted by {self.username}'
