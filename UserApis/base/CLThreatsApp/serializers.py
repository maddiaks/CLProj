from rest_framework import serializers
from django.db import transaction, IntegrityError
from CLThreatsApp.models import Threat

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('id', 'ip_address', 'domainname', 'reverse_lookup', 'description')


class ThreatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('ip_address', 'domainname', 'reverse_lookup', 'description')

        @transaction.atomic
        def create(self, validated_data):
            print("Creating bulk threats")
            user_stream = validated_data['data']
            print(validated_data)

            return {}