from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Level(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    levels = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.__str__()
