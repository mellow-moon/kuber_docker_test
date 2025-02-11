import logging
from datetime import timedelta, datetime

from test_deploy_proj.celery import app
from rest_framework import serializers
from tasks.models import TaskModel


logger = logging.getLogger(__name__)


class TaskSerializer(serializers.ModelSerializer):
    """ Base task serializer class which performs field validations """

    class Meta:
        model = TaskModel
        fields = ("task_name", "task_id", "is_revoked")

    task_id = serializers.ReadOnlyField()
    is_revoked = serializers.ReadOnlyField(required=False)

    def create(self, validated_data):
        task_name = validated_data.get("task_name")

        schedule_time = datetime.now() + timedelta(seconds=50)
        res = app.send_task(task_name, args=[1, 2], eta=schedule_time)

        task_id = res.id
        validated_data["task_id"] = task_id

        return super().create(validated_data)
