from rest_framework import serializers

from users.serializers import model_serializers

from .models import (
    Jprincipios,
    Jprinciossubdivisiones,
    Jindicadores,
    Vindicators,
    Jvalores,
    Jobjetivos,
    JobjetivosValores,
    Vobjectivesvalues
)


@model_serializers(Jprincipios)
class JprincipiosSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jprinciossubdivisiones)
class JprinciossubdivisionesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jindicadores)
class JindicadoresSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jvalores)
class JvaloresSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jobjetivos)
class JobjetivosSerializer(serializers.ModelSerializer):
    pass


@model_serializers(JobjetivosValores)
class JobjetivosValoresSerializer(serializers.ModelSerializer):
    pass


# Serializers for database views

@model_serializers(Vindicators)
class VindicatorsSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Vobjectivesvalues)
class VobjectivesvaluesSerializer(serializers.ModelSerializer):
    pass


