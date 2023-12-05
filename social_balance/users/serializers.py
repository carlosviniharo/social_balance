from rest_framework import serializers

from .models import Jusuarios


def model_serializers(model_):
    def decorator(serializer_class):
        class ModelSerializer(serializer_class):
            class Meta:
                model = model_
                fields = "__all__"

        return ModelSerializer

    return decorator


@model_serializers(Jusuarios)
class JusuariosSerializer(serializers.ModelSerializer):
    pass
