from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adopt_assignment.views import AssignmentViewSet

app_name = "adopt_assignment"

router = DefaultRouter()
router.register("assignment", AssignmentViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
