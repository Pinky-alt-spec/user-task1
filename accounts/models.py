from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    idnumber = models.IntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='man.jpeg', upload_to='images')
    # idcopy = models.FileField(upload_to='Profile_docs')
    # proofofaddress = models.FileField(upload_to='Profile_docs')

    def __str__(self):
        return f'{self.user.username}--Profile'

