from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class GeoJSONIncidentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [instance.longitude, instance.latitude]
            },
            "properties": {
                "id": instance.id,
                "title": instance.title,
                "status": instance.status,
                "created_at": instance.created_at.isoformat()
            }
        }

    class Meta:
        model = Incident
        fields = ('id', 'title', 'latitude', 'longitude', 'status', 'created_at')
