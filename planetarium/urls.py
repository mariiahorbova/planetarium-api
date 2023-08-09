from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet,
    ShowThemeViewSet,
    ShowSessionViewSet,
)

router = routers.DefaultRouter()
router.register("themes", ShowThemeViewSet)
router.register("planetariums", PlanetariumDomeViewSet)
router.register("shows", AstronomyShowViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]


app_name = "planetarium"
