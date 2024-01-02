from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    JprincipiosReadView,
    JprincipiosActiveView,
    JprincipiosIdView,
    JprincipiosSetView,
    JprinciossubdivisionesViewSet,
    JprinciossubdivisionesReadView,
    JprinciossubdivisionesActiveView,
    JprinciossubdivisionesIdView,
    JindicadoresViewSet, VindicatorssReadView, VindicatorsActiveView, VindicatorsIdView, IndicatorsByPrinciplesView,
)

router = DefaultRouter()
router.register(r"Principles", JprincipiosSetView)
router.register(r"PrinciplesSubdivisions", JprinciossubdivisionesViewSet)
router.register(r"Indicators", JindicadoresViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

    # Principles urls
    path("allPrinciples/", JprincipiosReadView.as_view(), name="list-principles"),
    path("activePrinciples/", JprincipiosActiveView.as_view(), name="list-activeprinciples"),
    path("idPrinciples/<int:pk>/", JprincipiosIdView.as_view(), name="id-principles"),

    # Principles subdivision urls
    path(
        "allPrinciplesSubdivisions/",
        JprinciossubdivisionesReadView.as_view(),
        name="list-principlessubdivisions"
    ),
    path(
        "activePrinciplesSubdivisions/",
        JprinciossubdivisionesActiveView.as_view(),
        name="list-activeprinciplessubdivisions"
    ),
    path(
        "idPrinciplesSubdivisions/<int:pk>/",
        JprinciossubdivisionesIdView.as_view(),
        name="id-principlessubdivisions"
    ),

    # Indicators urls
    path(
        "allIndicators/",
        VindicatorssReadView.as_view(),
        name="list-indicators"
    ),
    path(
        "activeIndicators/",
        VindicatorsActiveView.as_view(),
        name="list-activeindicators"
    ),
    path(
        "idIndicators/<int:pk>/",
        VindicatorsIdView.as_view(),
        name="id-indicators"
    ),
    path(
        "indicatorsByPrinciples/",
        IndicatorsByPrinciplesView.as_view(),
        name="list-indicatorsbyprinciples",
    )
]

