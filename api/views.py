from django.shortcuts import redirect
from rest_framework import viewsets, generics
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from .models import Incident
from .serializers import IncidentSerializer, GeoJSONIncidentSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class ActiveIncidentsGeoJSONView(generics.ListAPIView):
    serializer_class = GeoJSONIncidentSerializer

    def get_queryset(self):
        return Incident.objects.filter(status='active')


schema_view = get_schema_view(
    title="Incident API",
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

def redirect_to_docs(request):
    print(request)
    return redirect('/api/docs')


