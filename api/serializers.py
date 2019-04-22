from rest_framework import serializers
from api.models import Discovery, Category, Comments
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = ('id','user','comment','discovery','timestamp')


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'title', 'icon')
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','first_name','last_name','username','email')

class DiscoverySerializer(serializers.ModelSerializer):
	categories_obj = CategorySerializer(many=True)
	comments = CommentSerializer(many=True)
	author = UserSerializer()

	class Meta:
		model = Discovery
		fields = ('id','timestamp','title','url','embed','channel_name','author','description','votes','thumbnail', 'categories_obj','comments','vote')
		depth=1

class DiscoveryCatalogSerializer(serializers.ModelSerializer):
	author = UserSerializer()
	class Meta:
		model = Discovery
		fields = ('id','timestamp','title','author','thumbnail','channel_name','votes')
		depth = 1
	