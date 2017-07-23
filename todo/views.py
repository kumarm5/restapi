from todo.serializers import TaskSerializer
from todo.models import Task
from rest_framework.generics import ListAPIView

class PostListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
