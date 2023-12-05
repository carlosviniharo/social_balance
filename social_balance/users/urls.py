from django.urls import path

from .views import CustomTokenObtainPairView, JusuariosCreateView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("createUser/", JusuariosCreateView.as_view(), name="create_user"),
]