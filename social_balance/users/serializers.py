from rest_framework import serializers

from .models import (
    Jusuarios,
    Jcorporaciones,
    Jdepartamentos,
    Jgeneros,
    Jgeografia,
    Jroles,
    Jsucursales,
    Jtiposidentificaciones, Jpaginas, Jprivilegios,
)


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


@model_serializers(Jcorporaciones)
class JcorporacionesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jdepartamentos)
class JdepartamentosSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jgeneros)
class JgenerosSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jgeografia)
class JgeografiaSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jroles)
class JrolesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jsucursales)
class JsucursalesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jtiposidentificaciones)
class JtiposidentificacionesSerializer(serializers.ModelSerializer):
    pass


@model_serializers(Jpaginas)
class JpaginasSerializers(serializers.ModelSerializer):
    pass


@model_serializers(Jprivilegios)
class JprivilegiosSerizalizers(serializers.ModelSerializer):
    pass
