from rest_framework import serializers

from reports.models import Jreportes, JreportesObjetivosValores, Vprinciplesbyreports
from users.serializers import model_serializers


@model_serializers(Jreportes)
class JreportesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(JreportesObjetivosValores)
class JreportesObjetivosValoresSerializer(serializers.ModelSerializer):
    pass


# Serializers of the database views
@model_serializers(Vprinciplesbyreports)
class VprinciplesbyreportsSerializer(serializers.ModelSerializer):
    pass
