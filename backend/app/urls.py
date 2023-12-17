from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewTasksAPIView,TaskModelViewSet

router = DefaultRouter()
router.register('tasks', TaskModelViewSet)

urlpatterns = [
    path('',ViewTasksAPIView.as_view())
] + router.urls