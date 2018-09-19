from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Q
from CLThreatsApp.models import Threat
from .serializers import ThreatSerializer, ThreatCreateSerializer
from rest_framework.response import Response
from UserApis import utils


class CreateListMixin:
    """Allows bulk creation of a resource."""

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)


class ThreatView(CreateListMixin, viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

    # def get_serializer_class(self):
    #     serializer_class = self.serializer_class
    #
    #     if self.request.method == 'POST':
    #         serializer_class = ThreatCreateSerializer
    #
    #     return serializer_class

    # def create(self, request, *args, **kwargs):
    #     pass


class UrlCheckView(APIView):
    def get(self, request, hostname=None, original_path=None):

        print("Request.Data: {}, HostName: {}, Original Path: {}".format(
              request.data, hostname, original_path))
        full_url = hostname
        query_string = request.META['QUERY_STRING']
        if query_string:
            full_url += u'?' + query_string
        print("Final Hostname: ", full_url)

        result = utils.extract_domain_name(full_url)
        print(result)
        db_threat_obj = Threat.objects.all()

        data = {'status': True}

        for item in result:
            querySet = Threat.objects.filter(Q(ip_address__iexact=item) | Q(domainname__iexact=item))
            if len(querySet) >= 1:
                data['status'] = False
                break

        return Response(data)

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
