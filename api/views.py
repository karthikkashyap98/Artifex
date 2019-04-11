from django.shortcuts import render
from api.models import Discovery
from api.serializers import DiscoverySerializer
from rest_framework import viewsets


class DiscoveryView(viewsets.ModelViewSet):
	queryset = Discovery.objects.all()
	serializer_class = DiscoverySerializer

	

