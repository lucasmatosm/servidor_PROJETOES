from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image_url = models.CharField(max_length=100, blank=True, default='')

class Tinvestido(models.Model):
    data = models.DateTimeField()
    horas = models.IntegerField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_usuario')