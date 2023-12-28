from rest_framework import serializers

from users.serializers import model_serializers

from .models import Jprincipios, Jprinciossubdivisiones, Jindicadores


@model_serializers(Jprincipios)
class JprincipiosSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jprinciossubdivisiones)
class JprinciossubdivisionesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jindicadores)
class JindicadoresSerializer(serializers.ModelSerializer):
    pass

