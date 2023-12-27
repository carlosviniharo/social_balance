from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Jprincipios
from .serializers import JprincipiosSerializer
from users.utils.helper import (
    CustomPagination,
    BaseListView,
    BaseRetrieveView,
    BaseUpdateView,
)


class JprincipiosReadView(ListAPIView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class JprincipiosActiveView(BaseListView):
    serializer_class = JprincipiosSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Jprincipios.objects.filter(status=True)


class JprincipiosIdView(BaseRetrieveView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    permission_classes = (IsAuthenticated,)


class JprincipiosUpdateView(BaseUpdateView):
    serializer_class = JprincipiosSerializer
    queryset = Jprincipios.objects.all()
    permission_classes = (IsAuthenticated,)
