import uuid
import socket
import requests
from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework import status, viewsets
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def get_mac_address():
    # Get the MAC address of the computer
    mac_address = ":".join(
        ["{:02x}".format((uuid.getnode() >> ele) & 0xFF) for ele in range(0, 48, 8)]
    )
    return mac_address


def get_public_ip_address():
    # Method 1: Use a public API to get the IP address
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip")
    except requests.RequestException:
        pass

    # Method 2: Use a socket to connect to a remote server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error:
        pass

    return None


def c(search_string, model, fields=None):
    """
    This function search a specific string through the entire table/object
    using a SearchVector.
    :param search_string: str
    :param model: ORM object
    :param: array of the names of the columns to search in: list
    :return: query object
    """
    if search_string is not None and search_string != '':
        if not fields:
            fields = [field.name for field in model._meta.fields]
        query = SearchQuery(search_string)
        vector = SearchVector(*fields)
        return model.objects.annotate(search=vector).filter(search=query)
    return model.objects.all()


def get_query_by_id(parm_name, param_value, model):
    """
    Gets the query that matches a specific id in the model.
    :param parm_name: str
    :param param_value: str
    :param model: ORM object
    :return: query object
    """
    if param_value is None or param_value == "":
        raise APIException(f"{parm_name} not provided")
    return model.objects.filter(**{parm_name: param_value})


# Customize pagination output style class
class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

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


# Create view with customized Response
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
            status=status.HTTP_201_CREATED
            )


# List view with customized Response
class BaseListView(ListAPIView):
    """
    Base class for update views.
    """
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
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


# Viewset with customized Response

class BaseViewSet(viewsets.ModelViewSet):
    """
    Base class for set views.
    """

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_201_CREATED
            )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                "message": "success",
                "data": response.data
            },
            status=status.HTTP_200_OK
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        instance_data = self.get_serializer(instance)
        return Response({
            "message": "success",
            "data": instance_data.data
        }, status=status.HTTP_202_ACCEPTED)
