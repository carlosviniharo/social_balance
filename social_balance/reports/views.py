from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import Jreportes, JreportesObjetivosValores
from reports.serializers import JreportesSerializer, JreportesObjetivosValoresSerializer
from users.utils.helper import BaseViewSet, CustomPagination, BaseListView, BaseRetrieveView


# Reports API endpoints

class JreportesViewSet(BaseViewSet):
    serializer_class = JreportesSerializer
    queryset = Jreportes.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serialized_report = self.get_serializer(data=request.data)
        serialized_report.is_valid(raise_exception=True)
        report = serialized_report.validated_data
        local_time = timezone.localtime(timezone.now())
        report["titulo"] += f" {str(local_time.strftime('%Y-%m-%d %H:%M:%S'))}"
        new_report = Jreportes.objects.create(**report)
        response_report = self.get_serializer(new_report)
        return Response(
            {
                "message": "success",
                "data": response_report.data
            },
            status=status.HTTP_201_CREATED
            )


# Read services for Reportes

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


# Reports API endpoints

class JreportesObjetivosValoresViewSet(BaseViewSet):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer_reportobjvals = self.get_serializer(data=request.data, many=True)

        serializer_reportobjvals.is_valid(raise_exception=True)

        serializer_reportobjvals_objects = [
            JreportesObjetivosValores(**reportobjval)
            for reportobjval in serializer_reportobjvals.validated_data if reportobjval.get('idobjetivevalue').status
        ]

        # for reportobjval in serializer_reportobjvals.validated_data:
        #     if reportobjval.get('idobjetivevalue').status:
        #         JreportesObjetivosValores(**reportobjval)

        JreportesObjetivosValores.objects.bulk_create(serializer_reportobjvals_objects)

        return Response(
            {
                "message": "success",
                "data": "Reports created successfully",
            },
            status=status.HTTP_201_CREATED
        )


# Read services for ReportesObjetivosValores

class JreportesObjetivosValoresViewSetReadView(ListAPIView):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


# class JreportesObjetivosValoresActiveView(BaseListView):
#     serializer_class = JreportesObjetivosValoresSerializer
#     queryset = JreportesObjetivosValores.objects.filter(status=True)
#     pagination_class = None
#     permission_classes = (IsAuthenticated,)


class JreportesObjetivosValoresIdView(BaseRetrieveView):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.all()
    permission_classes = (IsAuthenticated,)
