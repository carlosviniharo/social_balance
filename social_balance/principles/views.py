from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.utils.helper import (
    CustomPagination,
    BaseListView,
    BaseRetrieveView,
    BaseViewSet,
    get_query_by_id,
    get_query,
)

from .models import Jprincipios, Jprinciossubdivisiones, Jindicadores, Vindicators, Jvalores, Jobjetivos, \
    JobjetivosValores, Vobjectivesvalues
from .serializers import (
    JprincipiosSerializer,
    JprinciossubdivisionesSerializer,
    JindicadoresSerializer,
    VindicatorsSerializer,
    JvaloresSerializer, JobjetivosSerializer, JobjetivosValoresSerializer, VobjectivesvaluesSerializer
)
from .utils.helper import get_result_accomplishment


#  Jprincipios API endpoints

class JprincipiosSetView(BaseViewSet):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    permission_classes = (IsAuthenticated,)


# Read services for Jprincipios
class JprincipiosReadView(ListAPIView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JprincipiosActiveView(BaseListView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JprincipiosIdView(BaseRetrieveView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    permission_classes = (IsAuthenticated,)


#  Jprinciossubdivisiones API endpoints

class JprinciossubdivisionesViewSet(BaseViewSet):
    queryset = Jprinciossubdivisiones.objects.all()
    serializer_class = JprinciossubdivisionesSerializer
    permission_classes = (IsAuthenticated,)


# Read services for Jprinciossubdivisiones

class JprinciossubdivisionesReadView(ListAPIView):
    serializer_class = JprinciossubdivisionesSerializer
    queryset = Jprinciossubdivisiones.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JprinciossubdivisionesActiveView(BaseListView):
    serializer_class = JprinciossubdivisionesSerializer
    queryset = Jprinciossubdivisiones.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JprinciossubdivisionesIdView(BaseRetrieveView):
    serializer_class = JprinciossubdivisionesSerializer
    queryset = Jprinciossubdivisiones.objects.all()
    permission_classes = (IsAuthenticated,)


#  Indicators API endpoints

class JindicadoresViewSet(BaseViewSet):
    serializer_class = JindicadoresSerializer
    queryset = Jindicadores.objects.all()
    permission_classes = (IsAuthenticated,)


# Read services for vindicators

class VindicatorsReadView(ListAPIView):
    serializer_class = VindicatorsSerializer
    queryset = Vindicators.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class VindicatorsActiveView(BaseListView):
    serializer_class = VindicatorsSerializer
    queryset = Vindicators.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class VindicatorsIdView(BaseRetrieveView):
    serializer_class = VindicatorsSerializer
    queryset = Vindicators.objects.all()
    permission_classes = (IsAuthenticated,)


class VindicatorsByPrinciplesView(BaseListView):
    serializer_class = VindicatorsSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    idprincipio = None
    search_string = None

    def get_queryset(self):
        self.idprincipio = self.request.query_params.get("idprincipio")
        self.search_string = self.request.query_params.get("search_string", None)
        return get_query_by_id("idprincipio", self.idprincipio, Vindicators)

    def get_queryset_search(self):
        lookup_columns = ["codigoindicador", "descripcionindicador", "variables"]
        query = get_query(self.search_string, Vindicators, lookup_columns).filter(idprincipio=self.idprincipio)
        return query

    def list(self, request, *args, **kwargs):
        sorted_indicators = {}
        queryset = self.get_queryset()
        if self.search_string:
            queryset = self.get_queryset_search()

        for entry in queryset:
            serialized = self.get_serializer(entry)
            exist = sorted_indicators.get(entry.idclasificacion, None)
            if not exist:
                sorted_indicators[entry.idclasificacion] = {
                    "idclasificacion": entry.idclasificacion,
                    "descripcionclasificacion": entry.descripcionclasificacion,
                    "data": [serialized.data]
                }
            else:
                sorted_indicators[entry.idclasificacion]["data"].append(serialized.data)
        return Response(
            {
                "message": "success",
                "data": sorted_indicators.values()
            },
            status=status.HTTP_200_OK
        )


# Values API endpoints

class JvaloresViewSet(BaseViewSet):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    permission_classes = (IsAuthenticated,)


# Read services for Jvalores

class JvaloresReadView(ListAPIView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JvaloresActiveView(BaseListView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JvaloresIdView(BaseRetrieveView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    permission_classes = (IsAuthenticated,)


# Objectives API endpoints

class JobjetivosViewSet(BaseViewSet):
    serializer_class = JobjetivosSerializer
    queryset = Jobjetivos.objects.all()
    permission_classes = (IsAuthenticated,)


# Read services for Jobjetivos

class JobjetivosReadView(ListAPIView):
    serializer_class = JobjetivosSerializer
    queryset = Jobjetivos.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JobjetivosActiveView(BaseListView):
    serializer_class = JobjetivosSerializer
    queryset = Jobjetivos.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class JobjetivosIdView(BaseRetrieveView):
    serializer_class = JobjetivosSerializer
    queryset = Jobjetivos.objects.all()
    permission_classes = (IsAuthenticated,)


# objetivosValores API endpoints

class JobjetivosValoresViewSet(BaseViewSet):
    serializer_class = JobjetivosValoresSerializer
    queryset = JobjetivosValores.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        objectivesvalues_serializer = self.get_serializer(data=request.data)
        objectivesvalues_serializer.is_valid(raise_exception=True)
        data_objval = objectivesvalues_serializer.validated_data

        data_objval = get_result_accomplishment(data_objval)

        objetivosValores, created = JobjetivosValores.objects.get_or_create(**data_objval)

        if not created:
            # If the object already exists, handle it as a repeated record
            return Response(
                {
                    "message":
                        f"A record with the this information was already saved. ID {objetivosValores.idobjetivevalue}"
                },
                status=status.HTTP_409_CONFLICT
            )
        else:
            idobjectivo = objetivosValores.idobjectivo.idobjectivo

            (
                JobjetivosValores.objects
                .filter(idobjectivo=idobjectivo, status=True)
                .exclude(idobjetivevalue=objetivosValores.idobjetivevalue)
                .update(status=False, fechamodificacion=timezone.localtime(timezone.now()))
             )

        serialized_objval = self.get_serializer(objetivosValores)
        return Response(
            {
                "message": "success",
                "data": serialized_objval.data
            },
            status=status.HTTP_201_CREATED
        )


# Read services for Jobjetivos

class VobjectivesvaluesReadView(ListAPIView):
    serializer_class = VobjectivesvaluesSerializer
    queryset = Vobjectivesvalues.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class VobjectivesvaluesActiveView(BaseListView):
    serializer_class = VobjectivesvaluesSerializer
    queryset = Vobjectivesvalues.objects.filter(status=True)
    pagination_class = None
    permission_classes = (IsAuthenticated,)


class VobjectivesvaluesIdView(BaseRetrieveView):
    serializer_class = VobjectivesvaluesSerializer
    queryset = Vobjectivesvalues.objects.all()
    permission_classes = (IsAuthenticated,)
