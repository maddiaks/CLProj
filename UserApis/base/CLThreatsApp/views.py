from rest_framework import viewsets
from rest_framework.views import APIView
from CLThreatsApp.models import Threat
from .serializers import ThreatSerializer
from rest_framework.response import Response


class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

class ThreatView(CreateListMixin, viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

# class ListThreat(APIView):
#     def get(self, request, format=None):
#         threat_objects = Threat.objects.all()
#         serializer = ThreatSerializer(threat_objects, many=True)
#         return Response(serializer.data)

# class ListThreat(APIView):
#     def get(self, request):
#         data = Threat.objects.values('id', 'ip_address', 'domainname', 'urllink', 'created_at')
#         # data = cache.get('threat')
#         return Response(data)
#
#     def post(self, request, format=None):
#         serializer = ThreatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
