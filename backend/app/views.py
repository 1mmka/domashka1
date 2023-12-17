from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListAPIView

# контроллер класса
class ViewTasksAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
# метаконтроллер
class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer