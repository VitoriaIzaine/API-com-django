from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializers

def index(request):
    return render(request,'cursos/index.html')

class CursoAPIView(APIView):
    """
    Api Curso Legal
    """

    def get(self,request):
        dados = Curso.objects.all()
        serializado = CursoSerializers(dados,many=True)
        return Response(serializado.data)
    def post(self,request):
        serializado = CursoSerializers(data=request.data)
        serializado.is_valid(raise_exception=True)
        serializado.save()
        return Response(serializado.data)