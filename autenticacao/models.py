from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True, null=True)
    # add additional fields in here
    def __str__(self):
       return self.username