from rest_framework import serializers
from api.models import Discovery


class DiscoverySerializer(serializers.ModelSerializer):
	class Meta:
		model = Discovery
		fields = ('id','title','url','channel_name','description','votes')


	
