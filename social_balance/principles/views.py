from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.utils.helper import (
    CustomPagination,
    BaseListView,
    BaseRetrieveView,
    BaseViewSet,
    get_query_by_id,
)

from .models import Jprincipios, Jprinciossubdivisiones, Jindicadores, Vindicators, Jvalores
from .serializers import (
    JprincipiosSerializer,
    JprinciossubdivisionesSerializer,
    JindicadoresSerializer,
    VindicatorsSerializer,
    JvaloresSerializer
)


#  Jprincipios API endpoints

class JprincipiosSetView(BaseViewSet):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    # permission_classes = (IsAuthenticated,)


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
    permissions_class = (IsAuthenticated,)


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

    def get_queryset(self):
        idprincipio = self.request.query_params.get("idprincipio")
        return get_query_by_id("idprincipio", idprincipio, Vindicators)


# Values API endpoints

class JvaloresViewSet(BaseViewSet):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    permissions_class = (IsAuthenticated,)


# Read services for Jvalores

class JvaloresReadView(ListAPIView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)


class JvaloresActiveView(BaseListView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.filter(status=True)
    pagination_class = None
    # permission_classes = (IsAuthenticated,)


class JvaloresIdView(BaseRetrieveView):
    serializer_class = JvaloresSerializer
    queryset = Jvalores.objects.all()
    # permission_classes = (IsAuthenticated,)
