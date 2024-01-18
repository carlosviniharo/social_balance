from rest_framework import serializers

from reports.models import Jreportes, JreportesObjetivosValores
from users.serializers import model_serializers


@model_serializers(Jreportes)
class JreportesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(JreportesObjetivosValores)
class JreportesObjetivosValoresSerializer(serializers.ModelSerializer):
    pass