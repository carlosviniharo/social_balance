from django.urls import path

from .views import (
    JprincipiosReadView,
    JprincipiosActiveView,
    JprincipiosIdView,
    JprincipiosUpdateView,
)

urlpatterns = [
    path("allPrinciples/", JprincipiosReadView.as_view(), name="list-principles"),
    path("activePrinciples/", JprincipiosActiveView.as_view(), name="list-activeprinciples"),
    path("idPrinciples/<int:pk>/", JprincipiosIdView.as_view(), name="id-principles"),
    path("updatePrinciples/<int:pk>/", JprincipiosUpdateView.as_view(), name="update-principles"),
]

