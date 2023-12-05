from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Jusuarios
from .serializers import JusuariosSerializer


class JusuariosCreateView(GenericAPIView):
    queryset = Jusuarios.objects.all()
    serializer_class = JusuariosSerializer
    
    def post(self, request, *args, **kwargs):
        usuario_serializer = JusuariosSerializer(data=request.data)
        usuario_serializer.is_valid(raise_exception=True)
        usuario_serializer.save()
        return Response(
            usuario_serializer.data,
            status=status.HTTP_201_CREATED,
        )
    # def list(self, request, *args, **kwargs):


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    An endpoint to login users.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            # Update the last_login field for the user upon successful login
            user = Jusuarios.objects.get(email=request.data["email"])
            user.last_login = timezone.now()
            user.save()

        return response
