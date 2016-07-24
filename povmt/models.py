from django.db import models
from povmt.utils import download_path


class Usuario(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    url_foto  = models.CharField(max_length=100, blank=True, default='')


class Atividade(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='')
    categoria = models.CharField(max_length=100, blank=True, default='')
    prioridade = models.CharField(max_length=100, blank=True, default='')
    url_imagem = models.ImageField(upload_to=download_path, default="media/No-img.jpg", null=True, blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    def __unicode__(self):
        return  str(self.id)


class Tinvestido(models.Model):
    data = models.CharField(max_length=100, blank=True, default='')
    semana = models.IntegerField()
    horas = models.IntegerField()
    id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, db_column='id_atividade')

class Tag(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='')
    id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, db_column='id_atividade')
