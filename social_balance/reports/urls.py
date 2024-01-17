from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reports.views import (
    JreportesViewSet,
    JreportesReadView,
    JreportesActiveView,
    JreportesIdView
)

router = DefaultRouter()

router.register(r"Reports", JreportesViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "allReports/", JreportesReadView.as_view(), name="list-allreports"
    ),
    path(
        "activeReports/", JreportesActiveView.as_view(), name="list-activereports"
    ),
    path(
        "idReports/<int:pk>/", JreportesIdView.as_view(), name="id-reports"
    ),
]
