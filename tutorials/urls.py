from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "tutorials"

router = routers.SimpleRouter()
router.register("", views.TutorialViewSet)

urlpatterns = [path("", include(router.urls))]
