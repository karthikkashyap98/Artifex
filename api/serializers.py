from rest_framework import serializers
from api.models import Discovery, Category, Comments

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = ('id','user','comment','discovery')


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'title', 'icon')

class DiscoverySerializer(serializers.ModelSerializer):
	categories_obj = CategorySerializer(many=True)
	comments = CommentSerializer(many=True)
	class Meta:
		model = Discovery
		fields = ('id','timestamp','title','url','channel_name','description','votes','thumbnail', 'categories_obj','comments')
		depth=1

class DiscoveryCatalogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discovery
		fields = ('id','timestamp','title','thumbnail','votes')
	