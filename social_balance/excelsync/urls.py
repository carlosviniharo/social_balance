from django.urls import path
from excelsync.views import ExcelsyncCreateView

urlpatterns = [
    path(
        "exceldigester/", ExcelsyncCreateView.as_view(), name="create-excelsync"
    ),
    ]
