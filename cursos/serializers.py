from rest_framework import serializers
from .models import Curso

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'descricao')