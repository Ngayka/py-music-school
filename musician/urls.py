from django.urls import include, path
from rest_framework import routers
from musician.views import MusicianViewSet


app_name = "musician"

router = routers.DefaultRouter()
router.register("musician", MusicianViewSet, basename="musician")


urlpatterns = [path("manage-list/", include(router.urls))]
