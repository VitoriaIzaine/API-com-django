from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)


    class Meta:
        verbose_name = 'Curso'

    def __str__(self):
        return self.nome
