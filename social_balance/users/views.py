from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

from .models import Jusuarios
from .serializers import JusuariosSerializer


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


class JusuariosCreateListView(ListCreateAPIView):
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
    
    def get_queryset(self):
        self.idusuario = self.request.query_params.get("idusuario", None)
        if self.idusuario is not None:
            return Jusuarios.objects.filter(idusuario=self.idusuario)
        return Jusuarios.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            # Apply pagination to the queryset
            page = self.paginate_queryset(queryset)
            user = JusuariosSerializer(page, many=True)
            return self.get_paginated_response(user.data)
        return Response({
            "message": f"User with Id {self.idusuario} not found",
        },
            status=status.HTTP_404_NOT_FOUND,
        )


# Create your views here.
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
