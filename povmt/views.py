from rest_framework.response import Response
from rest_framework.views import APIView
# coding=utf-8
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models  import *

from serializers import *

@api_view(['GET', 'PUT'])
def manipula_usuario(request, id):
    if request.method == 'GET':
        usuario = User.objects.get(pk=id)
        serializer = UserSerializer(usuario, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        usuario = User.objects.get(pk=id)
        data = request.data
        serializer = UserSerializer(instance=usuario, data=data)
        if serializer.is_valid():
            serializer.update(usuario, data)
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_usuario(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.create(data)
        id = {'id': user.pk}
        return Response(status=201, data=id)
    return Response(serializer.errors, status=400)


@api_view(['GET','POST'])
def criati(request, id_usuario):
    if request.method == 'GET':
        tilist = Tinvestido.objects.get(id_usuario=id_usuario)
        serializer = TISerializerID(tilist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data['id_usuario'] = id_usuario
        serializer = TISerializerID(data=data)
        if serializer.is_valid():
            ti = serializer.save()

            data = {
            'ti_id': ti.pk
            }
            return Response(status=201, data=data)
        return Response(serializer.errors, status=400)



