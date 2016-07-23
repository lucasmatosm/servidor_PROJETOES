from rest_framework import serializers

from povmt.models import User
from povmt.models import Tinvestido



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'image_url', 'id')


class UserSerializerID(serializers.ModelSerializer):
    class Meta:
        model = User


class TIserializer(serializers.ModelSerializer):
    class Meta:
        model = Tinvestido
        fields = ('data', 'horas', 'id_usuario')

class TISerializerID(serializers.ModelSerializer):
    class Meta:
        model = Tinvestido

