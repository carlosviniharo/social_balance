from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

from .utils.helper import get_query

from .models import Jusuarios, Jcorporaciones, Jdepartamentos, Jgeneros, Jgeografia, Jroles
from .serializers import JusuariosSerializer, JcorporacionesSerializer, JdepartamentosSerializer, JgenerosSerializer, \
    JgeografiaSerializer, JrolesSerializer


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


# CRUD services Corporation

class JusuariosCreateView(CreateAPIView):
    serializer_class = JusuariosSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    idusuario = None
    
    def create(self, request, *args, **kwargs):
        
        usuario_serializer = JusuariosSerializer(data=request.data)
        usuario_serializer.is_valid(raise_exception=True)
        Jusuarios.objects.create_user(**usuario_serializer.data)
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


class JusuariosActiveView(ListCreateAPIView):
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


class JusuariosUpdateView(UpdateAPIView):
    serializer_class = JusuariosSerializer
    queryset = Jusuarios.objects.all()
    # permission_classes = (IsAuthenticated,)


class JusuariosDeactivateView(DestroyAPIView):
    serializer_class = JusuariosSerializer
    queryset = Jusuarios.objects.all()
    # permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()

        serializer = JusuariosSerializer(user)
        return Response({
            "message": f"success",
            "data": serializer.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services Corporation

class JcorporacionesCreateView(CreateAPIView):
    serializer_class = JcorporacionesSerializer
    queryset = Jcorporaciones.objects.all()
    permission_classes = (IsAuthenticated,)


class JcorporacionesReadView(ListCreateAPIView):
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


class JcorporacionesActiveView(ListCreateAPIView):
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


class JcorporacionesUpdateView(UpdateAPIView):
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

class JdepartamentosCreateView(CreateAPIView):
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


class JdepartamentosActiveView(ListCreateAPIView):
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


class JdepartamentosUpdateView(UpdateAPIView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)


class JdepartamentosDeactivateView(DestroyAPIView):
    serializer_class = JdepartamentosSerializer
    queryset = Jdepartamentos.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request, *args, **kwargs):
        branch = self.get_object()
        branch.status = False
        branch.save()
        branch_data = JdepartamentosSerializer(branch)
        return Response({
            "message": f"success",
            "data": branch_data.data
        }, status=status.HTTP_202_ACCEPTED)


# CRUD services Genders

class JgenerosCreateView(CreateAPIView):
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


class JgenerosActiveView(ListCreateAPIView):
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


class JgenerosUpdateView(UpdateAPIView):
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

class JgeografiaCreateView(CreateAPIView):
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


class JgeografiaActiveView(ListCreateAPIView):
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


class JgeografiaUpdateView(UpdateAPIView):
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

class JrolesCreateView(CreateAPIView):
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


class JrolesActiveView(ListCreateAPIView):
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
