from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reports.models import Jreportes, JreportesObjetivosValores, Vprinciplesbyreports
from reports.serializers import (
    JreportesSerializer,
    JreportesObjetivosValoresSerializer,
    VprinciplesbyreportsSerializer
)
from users.utils.helper import BaseViewSet, CustomPagination, BaseListView, BaseRetrieveView, get_query_by_id


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

        with transaction.atomic():
            new_report, created = Jreportes.objects.get_or_create(**report)
            (Jreportes.objects
             .filter(status=True)
             .exclude(idreporte=new_report.idreporte)
             .update(status=False))

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
        report = request.data["report"]
        objetivevals = request.data["objetivevals"]
        serializer_reportobjvals = self.get_serializer(
            data=[{"idreporte": report, "idobjetivevalue": objetiveval} for objetiveval in objetivevals],
            many=True
        )
        serializer_reportobjvals.is_valid(raise_exception=True)

        created_objects = 0
        invalidated_records = 0

        with transaction.atomic():

            for reportobjval in serializer_reportobjvals.validated_data:
                idobjetivevalue = reportobjval.get('idobjetivevalue')

                if idobjetivevalue.is_complete:
                    created_objects += (
                        1
                        if JreportesObjetivosValores.objects.get_or_create(**reportobjval)[1]
                        else 0
                    )
                else:
                    raise APIException(
                        f"The ObjeviteValues number {reportobjval.get('idobjetivevalue').idobjetivevalue} "
                        f"is either incomplete or deactivated"
                    )

            invalidated_records = (
                JreportesObjetivosValores.objects
                .filter(idobjetivevalue__status=False)
                .update(status=False, fechamodificacion=timezone.localtime(timezone.now()))
            )

        return Response(
            {
                "message":  f"{created_objects} Reports were created successfully and "
                            f"{invalidated_records} records were invalidated."
            },
            status=status.HTTP_201_CREATED
        )


# Read services for ReportesObjetivosValores

class JreportesObjetivosValoresViewSetReadView(ListAPIView):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JreportesObjetivosValoresActiveView(BaseListView):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JreportesObjetivosValoresIdView(BaseRetrieveView):
    serializer_class = JreportesObjetivosValoresSerializer
    queryset = JreportesObjetivosValores.objects.all()
    permission_classes = (IsAuthenticated,)


class VprinciplesbyreportsView(ListAPIView):
    serializer_class = VprinciplesbyreportsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        idreporte = self.request.query_params.get("idreporte")
        return get_query_by_id("idreporte", idreporte, Vprinciplesbyreports)

