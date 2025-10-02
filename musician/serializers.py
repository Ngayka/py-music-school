from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"


class MusicianListSerializer(MusicianSerializer):
    is_adult = serializers.BooleanField(read_only=True)
