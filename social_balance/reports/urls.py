from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reports.views import (
    JreportesViewSet,
    JreportesReadView,
    JreportesActiveView,
    JreportesIdView,
    JreportesObjetivosValoresViewSet,
    JreportesObjetivosValoresViewSetReadView,
    # JreportesObjetivosValoresActiveView,
    JreportesObjetivosValoresIdView,
    VprinciplesbyreportsView,
    JreportesbyusersView,
    GenerateReport,
)

router = DefaultRouter()

# url for set view services.
router.register(r"Reports", JreportesViewSet)
router.register(r"ReportObjVals", JreportesObjetivosValoresViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

    # Reports urls
    path(
        "allReports/", JreportesReadView.as_view(), name="list-allreports"
    ),
    path(
        "activeReports/", JreportesActiveView.as_view(), name="list-activereports"
    ),
    path(
        "idReports/<int:pk>/", JreportesIdView.as_view(), name="id-reports"
    ),

    # JreportesObjetivosValores urls
    path(
        "allReportObjVals/", JreportesObjetivosValoresViewSetReadView.as_view(), name="list-reportobjvals"
    ),
    # path(
    #     "activeReportObjVals/", JreportesObjetivosValoresActiveView.as_view(), name="list-activereportobjvals"
    # ),
    path(
        "idReportObjVals/<int:pk>/", JreportesObjetivosValoresIdView.as_view(), name="id-reportobjvals"
    ),
    path(
        "principlesByReports/", VprinciplesbyreportsView.as_view(), name="list-principlesbyreports"
    ),
    path(
        "reportsByUsers/", JreportesbyusersView.as_view(), name="list-reportsbyusers"
    ),
    # Endpoint to generates a Word Document
    path(
        "generateDocx/", GenerateReport.as_view(), name="generate-docx"
    )
]
