from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    JusuariosCreateView,
    JusuariosReadView,
    JcorporacionesCreateView,
    JcorporacionesReadView,
    JcorporacionesUpdateView,
    JcorporacionesDeactivateView,
    JcorporacionesActiveView,
    JusuariosActiveView,
    JdepartamentosCreateView,
    JdepartamentosReadView,
    JusuariosDeactivateView,
    JusuariosUpdateView,
    JdepartamentosActiveView,
    JdepartamentosUpdateView,
    JdepartamentosDeactivateView,
    JgenerosCreateView,
    JgenerosReadView,
    JgenerosActiveView,
    JgenerosUpdateView,
    JgenerosDeactivateView,
    JgeografiaCreateView,
    JgeografiaReadView,
    JgeografiaActiveView,
    JgeografiaUpdateView,
    JgeografiaDeactivateView,
    JrolesCreateView,
    JrolesReadView,
    JrolesActiveView,
    JrolesUpdateView,
    JrolesDeactivateView,
)


urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # CRUD services Users
    path("createUsers/", JusuariosCreateView.as_view(), name="create_users"),
    path("allUsers/", JusuariosReadView.as_view(), name="list_users"),
    path("activeUsers/", JusuariosActiveView.as_view(), name="list-activeusers"),
    path("updateUsers/<int:pk>/", JusuariosUpdateView.as_view(), name="update-users"),
    path("deleteUsers/<int:pk>/", JusuariosDeactivateView.as_view(), name="delete-users"),
    # CRUD services Corporation
    path("createCoporations/", JcorporacionesCreateView.as_view(), name="create-corporations"),
    path("allCorporations/", JcorporacionesReadView.as_view(), name="list-corporations"),
    path("activeCorporations/", JcorporacionesActiveView.as_view(), name="list-activecorporations"),
    path("updateCorporation/<int:pk>/", JcorporacionesUpdateView.as_view(), name="update-corporations"),
    path("deleteCorporation/<int:pk>/", JcorporacionesDeactivateView.as_view(), name="delete-corporations"),
    # CRUD services Department
    path("createDepartments/", JdepartamentosCreateView.as_view(), name="create-departments"),
    path("allDepartments/", JdepartamentosReadView.as_view(), name="list-departments"),
    path("activeDepartments/", JdepartamentosActiveView.as_view(), name="list-activedepartments"),
    path("updateDepartments/<int:pk>/", JdepartamentosUpdateView.as_view(), name="update-departments"),
    path("deleteDepartments/<int:pk>/", JdepartamentosDeactivateView.as_view(), name="delete-departments"),
    # CRUD services Gender
    path("createGenders/", JgenerosCreateView.as_view(), name="create-genders"),
    path("allGenders/", JgenerosReadView.as_view(), name="list-genders"),
    path("activeGenders/", JgenerosActiveView.as_view(), name="list-activegenders"),
    path("updateGenders/<int:pk>/", JgenerosUpdateView.as_view(), name="update-genders"),
    path("deleteGenders/<int:pk>/", JgenerosDeactivateView.as_view(), name="delete-genders"),
    # CRUD services Geography
    path("createGeography/", JgeografiaCreateView.as_view(), name="create-geography"),
    path("allGeography/", JgeografiaReadView.as_view(), name="list-geography"),
    path("activeGeography/", JgeografiaActiveView.as_view(), name="list-activegeography"),
    path("updateGeography/<int:pk>/", JgeografiaUpdateView.as_view(), name="update-geography"),
    path("deleteGeography/<int:pk>/", JgeografiaDeactivateView.as_view(), name="delete-geography"),
    # CRUD services Roles
    path("createRoles/", JrolesCreateView.as_view(), name="create-roles"),
    path("allRoles/", JrolesReadView.as_view(), name="list-roles"),
    path("activeRoles/", JrolesActiveView.as_view(), name="list-activeroles"),
    path("updateRoles/<int:pk>/", JrolesUpdateView.as_view(), name="update-roles"),
    path("deleteRoles/<int:pk>/", JrolesDeactivateView.as_view(), name="delete-roles"),
]
