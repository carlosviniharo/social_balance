from rest_framework import serializers


def model_serializers(model_):
    def decorator(serializer_class):
        class ModelSerializer(serializer_class):
            class Meta:
                model = model_
                fields = tuple(f.name for f in model_._meta.fields) + ("url",)

        return ModelSerializer

    return decorator