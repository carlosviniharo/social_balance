from django.utils import timezone
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed, APIException

from .utils.helper import get_query, get_query_by_id

from .models import (
    Jusuarios,
    Jcorporaciones,
    Jdepartamentos,
    Jgeneros,
    Jgeografia,
    Jroles,
    Jsucursales,
    Jtiposidentificaciones,
    Jpaginas,
    Jprivilegios,
    Vusuarios,
)
from .serializers import (
    JusuariosSerializer,
    JcorporacionesSerializer,
    JdepartamentosSerializer,
    JgenerosSerializer,
    JgeografiaSerializer,
    JrolesSerializer,
    JsucursalesSerializer,
    JtiposidentificacionesSerializer,
    JpaginasSerializer,
    JprivilegiosSerializer,
    VusuariosSerializer
)


# Customize pagination output style class
class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'message': 'success',
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page': self.page.number,
            'perPage': self.page.paginator.per_page,
            'totalPages': self.page.paginator.num_pages,
            'totalCount': self.page.paginator.count,
            'data': data
        })


# Update view with customized Create
class BaseCreateView(CreateAPIView):
    """
    Base class for update views.
    """
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_200_OK
            )


# Retrieve view with customized Response
class BaseRetrieveView(RetrieveAPIView):
    """
    Base class for retrieval views.
    """
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_200_OK
        )


# Update view with customized Response
class BaseUpdateView(UpdateAPIView):
    """
    Base class for update views.
    """
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_200_OK
            )


# CRUD services Users

class JusuariosCreateView(CreateAPIView):
    serializer_class = JusuariosSerializer
    queryset = Jusuarios.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        usuario_serializer = JusuariosSerializer(data=request.data)
        usuario_serializer.is_valid(raise_exception=True)
        Jusuarios.objects.create_user(**usuario_serializer.validated_data)

        return Response({
            "message": "success",
            "data": usuario_serializer.data
        },
            status=status.HTTP_201_CREATED,
        )


class JusuariosReadView(ListAPIView):
    serializer_class = JusuariosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jusuarios)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and search_string is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Corporation does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            users = self.get_serializer(page, many=True)
            return self.get_paginated_response(users.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any fild of Users",
        }, status=status.HTTP_404_NOT_FOUND
        )


class JusuariosActiveView(ListAPIView):
    serializer_class = JusuariosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jusuarios.objects.filter(is_active=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            users = JusuariosSerializer(page, many=True)
            return self.get_paginated_response(users.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JusuariosIdView(BaseRetrieveView):
    serializer_class = VusuariosSerializer
    queryset = Vusuarios.objects.all()
    permission_classes = (IsAuthenticated,)


class JusuariosUpdateView(BaseUpdateView):
    serializer_class = JusuariosSerializer
    queryset = Jusuarios.objects.all()
    permission_classes = (IsAuthenticated,)


class JusuariosDeactivateView(DestroyAPIView):
    serializer_class = JusuariosSerializer
    queryset = Jusuarios.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()

        serializer = JusuariosSerializer(user)
        return Response({
            "message": f"success",
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services Corporation

class JcorporacionesCreateView(BaseCreateView):
    serializer_class = JcorporacionesSerializer
    queryset = Jcorporaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JcorporacionesReadView(ListAPIView):
    serializer_class = JcorporacionesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None
    
    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jcorporaciones)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and idcorporaciones is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Corporation does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            corporaciones = JcorporacionesSerializer(page, many=True)
            return self.get_paginated_response(corporaciones.data)
        
        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Corporations",
        }, status=status.HTTP_404_NOT_FOUND)


class JcorporacionesActiveView(ListAPIView):
    serializer_class = JcorporacionesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jcorporaciones.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            corporaciones = JcorporacionesSerializer(page, many=True)
            return self.get_paginated_response(corporaciones.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JcorporacionesIdView(BaseRetrieveView):
    serializer_class = JcorporacionesSerializer
    queryset = Jcorporaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JcorporacionesUpdateView(BaseUpdateView):
    serializer_class = JcorporacionesSerializer
    queryset = Jcorporaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JcorporacionesDeactivateView(DestroyAPIView):
    serializer_class = JcorporacionesSerializer
    queryset = Jcorporaciones.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request, *args, **kwargs):
        corporation = self.get_object()
        corporation.status = False
        corporation.save()
        corpo_data = JcorporacionesSerializer(corporation)
        return Response({
            "message": "success",
            "data": corpo_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services Departments

class JdepartamentosCreateView(BaseCreateView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)


class JdepartamentosReadView(ListAPIView):
    serializer_class = JdepartamentosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jdepartamentos)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and departamentos is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jdepartmentos does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            departments = JdepartamentosSerializer(page, many=True)
            return self.get_paginated_response(departments.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jdepartamentos",
        }, status=status.HTTP_404_NOT_FOUND)


class JdepartamentosActiveView(ListAPIView):
    serializer_class = JdepartamentosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jdepartamentos.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            departamentos_data = JcorporacionesSerializer(page, many=True)
            return self.get_paginated_response(departamentos_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JdepartamentosIdView(BaseRetrieveView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)


class JdepartamentosUpdateView(BaseUpdateView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)


class JdepartamentosDeactivateView(DestroyAPIView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request, *args, **kwargs):
        depa = self.get_object()
        depa.status = False
        depa.save()
        depa_data = JdepartamentosSerializer(depa)
        return Response({
            "message": f"success",
            "data": depa_data.data
        }, status=status.HTTP_202_ACCEPTED)


class JdepartamentosByBranchesView(ListAPIView):
    serializer_class = JdepartamentosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        idsucursal = self.request.query_params.get("idsucursal", None)
        return get_query_by_id("idsucursal", idsucursal, Jdepartamentos)


# CRUD services Genders

class JgenerosCreateView(BaseCreateView):
    serializer_class = JgenerosSerializer
    queryset = Jgeneros.objects.all()
    permission_classes = (IsAuthenticated,)


class JgenerosReadView(ListAPIView):
    serializer_class = Jgeneros
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jgeneros)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jgeneros is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jgeneros does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            departments = JgenerosSerializer(page, many=True)
            return self.get_paginated_response(departments.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jgeneros",
        }, status=status.HTTP_404_NOT_FOUND)


class JgenerosActiveView(ListAPIView):
    serializer_class = JgenerosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jgeneros.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            generos_data = JgenerosSerializer(page, many=True)
            return self.get_paginated_response(generos_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JgenerosIdView(BaseRetrieveView):
    serializer_class = JgenerosSerializer
    queryset = Jgeneros.objects.all()
    permission_classes = (IsAuthenticated,)


class JgenerosUpdateView(BaseUpdateView):
    serializer_class = JgenerosSerializer
    queryset = Jgeneros.objects.all()
    permission_classes = (IsAuthenticated,)


class JgenerosDeactivateView(DestroyAPIView):
    serializer_class = JgenerosSerializer
    queryset = Jgeneros.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        gender = self.get_object()
        gender.status = False
        gender.save()
        gender_data = JgenerosSerializer(gender)
        return Response({
            "message": f"success",
            "data": gender_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services geography

class JgeografiaCreateView(BaseCreateView):
    serializer_class = JgeografiaSerializer
    queryset = Jgeografia.objects.all()
    permission_classes = (IsAuthenticated,)


class JgeografiaReadView(ListAPIView):
    serializer_class = Jgeografia
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jgeografia)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jgeneros is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jgeografia does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            geografia_data = JgeografiaSerializer(page, many=True)
            return self.get_paginated_response(geografia_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jgeografia",
        }, status=status.HTTP_404_NOT_FOUND)


class JgeografiaActiveView(ListAPIView):
    serializer_class = JgeografiaSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jgeografia.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            geografia_data = JgeografiaSerializer(page, many=True)
            return self.get_paginated_response(geografia_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JgeografiaIdView(BaseRetrieveView):
    serializer_class = JgeografiaSerializer
    queryset = Jgeografia.objects.all()
    permission_classes = (IsAuthenticated,)


class JgeografiaUpdateView(BaseUpdateView):
    serializer_class = JgeografiaSerializer
    queryset = Jgeografia.objects.all()
    permission_classes = (IsAuthenticated,)


class JgeografiaDeactivateView(DestroyAPIView):
    serializer_class = JgeografiaSerializer
    queryset = Jgeografia.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        geo = self.get_object()
        geo.status = False
        geo.save()
        geo_data = JgeografiaSerializer(geo)
        return Response({
            "message": f"success",
            "data": geo_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services roles

class JrolesCreateView(BaseCreateView):
    serializer_class = JrolesSerializer
    queryset = Jroles.objects.all()
    permission_classes = (IsAuthenticated,)


class JrolesReadView(ListAPIView):
    serializer_class = JrolesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jroles)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jroles is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jroles does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            role_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(role_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jroles",
        }, status=status.HTTP_404_NOT_FOUND)


class JrolesActiveView(ListAPIView):
    serializer_class = JrolesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jroles.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            role_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(role_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JrolesIdView(BaseRetrieveView):
    serializer_class = JrolesSerializer
    queryset = Jroles.objects.all()
    permission_classes = (IsAuthenticated,)


class JrolesUpdateView(UpdateAPIView):
    serializer_class = JrolesSerializer
    queryset = Jroles.objects.all()
    permission_classes = (IsAuthenticated,)


class JrolesDeactivateView(DestroyAPIView):
    serializer_class = JrolesSerializer
    queryset = Jroles.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        role = self.get_object()
        role.status = False
        role.save()
        role_data = self.get_serializer(role)
        return Response({
            "message": f"success",
            "data": role_data.data
        }, status=status.HTTP_202_ACCEPTED)


class JrolesByDepartmentsView(ListAPIView):
    serializer_class = JrolesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        iddepartamento = self.request.query_params.get("iddepartamento", None)
        return get_query_by_id("iddepartamento", iddepartamento, Jroles)


# CRUD services branches

class JsucursalesCreateView(BaseCreateView):
    serializer_class = JsucursalesSerializer
    queryset = Jsucursales.objects.all()
    permission_classes = (IsAuthenticated,)


class JsucursalesReadView(ListAPIView):
    serializer_class = JsucursalesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jsucursales)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jsucursales is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jsucursales does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            branch_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(branch_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jsucursales",
        }, status=status.HTTP_404_NOT_FOUND)


class JsucursalesActiveView(ListAPIView):
    serializer_class = JsucursalesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jsucursales.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            branch_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(branch_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JsucursalesIdView(BaseRetrieveView):
    serializer_class = JsucursalesSerializer
    queryset = Jsucursales.objects.all()
    permission_classes = (IsAuthenticated,)


class JsucursalesUpdateView(BaseUpdateView):
    serializer_class = JsucursalesSerializer
    queryset = Jsucursales.objects.all()
    permission_classes = (IsAuthenticated,)


class JsucursalesDeactivateView(DestroyAPIView):
    serializer_class = JsucursalesSerializer
    queryset = Jsucursales.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        brach = self.get_object()
        brach.status = False
        brach.save()
        brach_data = self.get_serializer(brach)
        return Response({
            "message": "success",
            "data": brach_data.data
        }, status=status.HTTP_202_ACCEPTED)


class JsucursalesByCorporationView(ListAPIView):
    serializer_class = JsucursalesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        idcorporacion = self.request.query_params.get("idcorporacion")
        return get_query_by_id("idcorporacion", idcorporacion, Jsucursales)


# CRUD services types of ID
class JtiposidentificacionesCreateView(BaseCreateView):
    serializer_class = JtiposidentificacionesSerializer
    queryset = Jtiposidentificaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JtiposidentificacionesReadView(ListAPIView):
    serializer_class = JtiposidentificacionesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jtiposidentificaciones)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jtiposidentificaciones is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jtiposidentificaciones does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            typeid_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(typeid_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of c",
        }, status=status.HTTP_404_NOT_FOUND)


class JtiposidentificacionesActiveView(ListAPIView):
    serializer_class = JtiposidentificacionesSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jtiposidentificaciones.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            typeid_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(typeid_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JtiposidentificacionesIdView(BaseRetrieveView):
    serializer_class = JtiposidentificacionesSerializer
    queryset = Jtiposidentificaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JtiposidentificacionesUpdateView(BaseUpdateView):
    serializer_class = JtiposidentificacionesSerializer
    queryset = Jtiposidentificaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JtiposidentificacionesDeactivateView(DestroyAPIView):
    serializer_class = JtiposidentificacionesSerializer
    queryset = Jtiposidentificaciones.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        typeid = self.get_object()
        typeid.status = False
        typeid.save()
        typeid_data = self.get_serializer(typeid)
        return Response({
            "message": f"success",
            "data": typeid_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services pages

class JpaginasCreateView(BaseCreateView):
    serializer_class = JpaginasSerializer
    queryset = Jpaginas.objects.all()
    permission_classes = (IsAuthenticated,)


class JpaginasReadView(ListAPIView):
    serializer_class = JpaginasSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jpaginas)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jpaginas is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jpaginas does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            page_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(page_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jpaginas",
        }, status=status.HTTP_404_NOT_FOUND)


class JpaginasActiveView(ListAPIView):
    serializer_class = JpaginasSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jpaginas.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            page_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(page_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JpaginasIdView(BaseRetrieveView):
    serializer_class = JpaginasSerializer
    queryset = Jpaginas.objects.all()
    permission_classes = (IsAuthenticated,)


class JpaginasUpdateView(BaseUpdateView):
    serializer_class = JpaginasSerializer
    queryset = Jpaginas.objects.all()
    permission_classes = (IsAuthenticated,)


class JpaginasDeactivateView(DestroyAPIView):
    serializer_class = JpaginasSerializer
    queryset = Jpaginas.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        page = self.get_object()
        page.status = False
        page.save()
        page_data = self.get_serializer(page)
        return Response({
            "message": f"success",
            "data": page_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services privileges

class JprivilegiosCreateView(BaseCreateView):
    serializer_class = JprivilegiosSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_201_CREATED
        )


class JprivilegiosReadView(ListAPIView):
    serializer_class = JprivilegiosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    search_string = None

    def get_queryset(self):
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query(self.search_string, Jprivilegios)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Check if the queryset is empty and Jprivilegios is not provided
        if not queryset.exists() and self.search_string is None:
            return Response({
                "message": "Jprivilegios does not have any records",
            }, status=status.HTTP_404_NOT_FOUND)

        # Apply pagination to the queryset
        page = self.paginate_queryset(queryset)

        if page is not None:
            priv_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(priv_data.data)

        return Response({
            "message": f"The string {self.search_string} was not found in "
                       f"any field of Jprivilegios",
        }, status=status.HTTP_404_NOT_FOUND)


class JprivilegiosActiveView(ListAPIView):
    serializer_class = JprivilegiosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Jprivilegios.objects.filter(status="True")
        page = self.paginate_queryset(queryset)
        if page is not None:
            priv_data = self.get_serializer(page, many=True)
            return self.get_paginated_response(priv_data.data)

        return Response({
            "message": f"No active records were found",
        }, status=status.HTTP_404_NOT_FOUND)


class JprivilegiosIdView(BaseRetrieveView):
    serializer_class = JprivilegiosSerializer
    queryset = Jprivilegios.objects.all()
    permission_classes = (IsAuthenticated,)


class JprivilegiosUpdateView(BaseUpdateView):
    serializer_class = JprivilegiosSerializer
    queryset = Jprivilegios.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_200_OK
        )


class JprivilegiosDeactivateView(DestroyAPIView):
    serializer_class = JprivilegiosSerializer
    queryset = Jprivilegios.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        page = self.get_object()
        page.status = False
        page.save()
        page_data = self.get_serializer(page)
        return Response({
            "message": f"success",
            "data": page_data.data
        }, status=status.HTTP_202_ACCEPTED)


class JprivilegiosByRolesView(ListAPIView):
    serializer_class = JprivilegiosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        idrol = self.request.query_params.get("idrol", None)
        return get_query_by_id("idrol", idrol, Jprivilegios)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    An endpoint to login users.
    """
    def post(self, request, *args, **kwargs):
        response = Response()

        try:
            response = super().post(request, *args, **kwargs)

            if response.status_code == 200:
                # Update the last_login field for the user upon successful login
                user = Jusuarios.objects.get(email=request.data["email"])
                user.last_login = timezone.now()
                user.save()
                response.data["name"] = user.first_name + user.last_name
                response.data["role"] = user.idrol.nombrerol if user.idrol else None
                response.data["email"] = user.email
                response.data["message"] = "success"

        except AuthenticationFailed as auth:
            response.status_code = auth.status_code
            if response.data is None:
                response.data = {}
            response.data["message"] = auth.detail
        return response
