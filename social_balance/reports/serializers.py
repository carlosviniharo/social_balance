from rest_framework import serializers

from reports.models import Jreportes
from users.serializers import model_serializers


@model_serializers(Jreportes)
class JreportesSerializer(serializers.ModelSerializer):
    pass
