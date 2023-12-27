from rest_framework import serializers

from users.serializers import model_serializers

from .models import Jprincipios


@model_serializers(Jprincipios)
class JprincipiosSerializer(serializers.ModelSerializer):
    pass


