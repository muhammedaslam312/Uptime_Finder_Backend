from rest_framework import serializers
from .models import Monitor, MonitorRequest,DeleteUrls


class MonitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monitor
        read_only_fields = ("id", "created_at")
        fields = (
            "id",
            "created_at",
            "endpoint",
            "interval",
        )


class MonitorRequestSerializer(serializers.ModelSerializer):
    monitor_endpoint = serializers.SerializerMethodField()

    def get_monitor_endpoint(self, obj):
        return obj.monitor.endpoint

    class Meta:
        model = MonitorRequest
        read_only_fields = ("id", "created_at")
        fields = (
            "id",
            "created_at",
            "response_time",
            "response_status",
            "monitor_endpoint",
            'monitor',
            'status',
        )

class DeleteUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model= DeleteUrls
        fields='__all__'