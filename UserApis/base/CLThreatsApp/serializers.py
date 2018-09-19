from rest_framework import serializers
from CLThreatsApp.models import Threat

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('id', 'ip_address', 'domainname', 'reverse_lookup', 'description')