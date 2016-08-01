from rest_framework.response import Response
from rest_framework.views import APIView
# coding=utf-8
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models  import *

from serializers import *

@api_view(['GET','POST'])
def cria_usuario(request):
    if request.method == 'GET':
        listuser = Usuario.objects.all()
        serializer = UsuarioSerializerID(listuser, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            data = {'id': user.pk}
            return Response(status=201, data=data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_usuario(request, id_usuario):
        user = Usuario.objects.get(pk=id_usuario)
        serializer = UsuarioSerializer(user, many=False)
        return Response(serializer.data)



@api_view(['GET','POST'])
def criaAtividade(request, id_usuario):
    if request.method == 'GET':
        if not request.GET._mutable:
            request.GET._mutable = True
        listActivity = Atividade.objects.filter(id_usuario=id_usuario)
        serializer = AtividadeSerializerID(listActivity, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.POST._mutable = True
        ##request.data['id_usuario'] = id_usuario
        serializer = AtividadeSerializer(data=request.data)
        print serializer
        if serializer.is_valid():
            ati = serializer.save()
            data = {
            'ati_id': ati.pk
            }
            return Response(status=201, data=data)
        return Response(serializer.errors, status=400)




@api_view(['GET','POST'])
def criaTI(request, id_atividade):
    if request.method == 'GET':
        if not request.GET._mutable:
            request.GET._mutable = True
        listTi = Tinvestido.objects.filter(id_atividade=id_atividade)
        serializer = TISerializerID(listTi, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.POST._mutable = True
        #request.data['id_atividade'] = id_atividade
        serializer = TISerializer(data=request.data)
        if serializer.is_valid():
            ti = serializer.save()

            data = {
                'ti_id': ti.pk
            }
            return Response(status=201, data=data)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT'])
def editaTI(request, id_atividade, id):
    if request.method == 'GET':
        if not request.GET._mutable:
            request.GET._mutable = True
        ti = Tinvestido.objects.get(pk=id)
        serializer = TISerializer(ti, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        ti = Tinvestido.objects.get(id_atividade=id_atividade, pk=id)
        request.data['id_atividade'] = id_atividade
        serializer = TISerializer(instance=ti, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','POST'])
def criaTag(request, id_atividade):
    if request.method == 'GET':
        if not request.GET._mutable:
            request.GET._mutable = True
        listTag = Tag.objects.filter(id_atividade=id_atividade)
        serializer = TagSerializerID(listTag, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.POST._mutable = True
        #request.data['id_atividade'] = id_atividade
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            ti = serializer.save()
            data = {
                'ti_id': ti.pk
            }
            return Response(status=201, data=data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def recuperaAti(request, id):
    if request.method == 'GET':
        if not request.GET._mutable:
            request.GET._mutable = True
        tag = Tag.objects.get(pk=id)
        atividade = Atividade.objects.get(pk=tag.id_atividade.id)
        serializer = AtividadeSerializer(atividade, many=False)
        return Response(serializer.data)



@api_view(['GET'])
def getAtividade(request, id):
        if not request.GET._mutable:
            request.GET._mutable = True
        ati = Atividade.objects.get(pk=id)
        print ati
        serializer = AtividadeSerializer(ati, many=False)
        return Response(serializer.data)
