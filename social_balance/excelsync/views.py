from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from excelsync.utils.helper import extract_excel_to_json
from principles.models import Jvalores
from principles.serializers import JvaloresSerializer


# Create your views here.

class ExcelsyncCreateView(CreateAPIView):
    queryset = Jvalores.objects.all()
    serializer_class = JvaloresSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        excel_file = request.FILES.get("excelfile")
        if excel_file:
            return Response(
                {
                    "detail": "success",
                    "data": extract_excel_to_json(excel_file)
                },
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {"detail": "No pdf file was provided or provided a corrupted one"},
                status=status.HTTP_400_BAD_REQUEST
            )
