from django.utils import timezone
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Jusuarios


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
