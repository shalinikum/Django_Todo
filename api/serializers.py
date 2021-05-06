from rest_framework import serializers
from task import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'complete',
            'created'
        )
        model = models.Task