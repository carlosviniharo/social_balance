from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import Jreportes
from reports.serializers import JreportesSerializer
from users.utils.helper import BaseViewSet, CustomPagination, BaseListView, BaseRetrieveView


# Create your views here.
class JreportesViewSet(BaseViewSet):
    serializer_class = JreportesSerializer
    queryset = Jreportes.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serialized_report = self.get_serializer(data=request.data)
        serialized_report.is_valid(raise_exception=True)
        report = serialized_report.validated_data
        report["titulo"] += f" {str(timezone.now().strftime('%Y-%m-%d %H:%M:%S'))}"
        new_report = Jreportes.objects.create(**report)
        response_report = self.get_serializer(new_report)
        return Response(
            {
                "message": "success",
                "data": response_report.data
            },
            status=status.HTTP_201_CREATED
            )


# Read services for Jprincipios
class JreportesReadView(ListAPIView):
    serializer_class = JreportesSerializer
    queryset = Jreportes.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JreportesActiveView(BaseListView):
    serializer_class = JreportesSerializer
    queryset = Jreportes.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JreportesIdView(BaseRetrieveView):
    serializer_class = JreportesSerializer
    queryset = Jreportes.objects.all()
    permission_classes = (IsAuthenticated,)


