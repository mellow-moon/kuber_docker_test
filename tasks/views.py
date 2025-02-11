import logging

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from tasks.models import TaskModel
from tasks.serializers import TaskSerializer

logger = logging.getLogger(__name__)


class TasksModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    This view creates all the required methods for list, create, and retrieve automatically.

    please have a look at this link: https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

    """

    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "task_id"

    def create(self, request, *args, **kwargs):
        """ Creates a new task

        - Create a new task in DB.
        """
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """ Lists all the available tasks

        - Show all the tasks and their details together.
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ Retrieve a task based on its database ID

        - Show all the task and their details together.
        """
        return super().retrieve(request, *args, **kwargs)
