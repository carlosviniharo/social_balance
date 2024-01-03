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
    JindicadoresViewSet,
    VindicatorsReadView,
    VindicatorsActiveView,
    VindicatorsIdView,
    VindicatorsByPrinciplesView,
    JvaloresViewSet,
    JvaloresReadView,
    JvaloresActiveView,
    JvaloresIdView, JobjetivosViewSet, JobjetivosReadView, JobjetivosActiveView, JobjetivosIdView,
    JobjetivosValoresViewSet,
)

router = DefaultRouter()
router.register(r"Principles", JprincipiosSetView)
router.register(r"PrinciplesSubdivisions", JprinciossubdivisionesViewSet)
router.register(r"Indicators", JindicadoresViewSet)
router.register(r"Values", JvaloresViewSet)
router.register(r"Objectives", JobjetivosViewSet)
router.register(r"objetivosValores", JobjetivosValoresViewSet)
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
        VindicatorsReadView.as_view(),
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
        VindicatorsByPrinciplesView.as_view(),
        name="list-indicatorsbyprinciples",
    ),

    # Values urls
    path(
        "allValues/",
        JvaloresReadView.as_view(),
        name="list-values",
    ),
    path(
        "activeValues/",
        JvaloresActiveView.as_view(),
        name="list-activevalues",
    ),
    path(
        "idValues/<int:pk>/",
        JvaloresIdView.as_view(),
        name="id-values",
    ),

    # Objectives urls
    path(
        "allObjectives/",
        JobjetivosReadView.as_view(),
        name="list-objectives",
    ),
    path(
        "activeObjectives/",
        JobjetivosActiveView.as_view(),
        name="list-activeobjectives",
    ),
    path(
        "idObjectives/<int:pk>/",
        JobjetivosIdView.as_view(),
        name="id-objectives",
    ),
]
