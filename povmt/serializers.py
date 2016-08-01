from rest_framework import serializers

from povmt.models import Usuario
from povmt.models import Tag
from povmt.models import Atividade
from povmt.models import Tinvestido


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'url_foto', 'id','data_created')

class UsuarioSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Usuario



class TISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tinvestido
        fields = ('data', 'semana', 'horas', 'id_atividade','id','data_created')

class TISerializerID(serializers.ModelSerializer):
    class Meta:
        model = Tinvestido


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('nome', 'id_atividade','id','data_created')

class TagSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Tag



class AtividadeSerializer(serializers.ModelSerializer):
    url_imagem = serializers.ImageField(max_length=None, required=False, use_url=True)
    class Meta:
        model = Atividade
        fields = ('nome', 'categoria', 'prioridade', 'url_imagem', 'id_usuario', 'id','data_created')

class AtividadeSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Atividade






