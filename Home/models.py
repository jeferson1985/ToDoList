from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)#toda tarefa sera atribuida a um  usuario
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    date = models.CharField(max_length=10)
    status = models.BooleanField()

    def __str__(self):
        return self.title