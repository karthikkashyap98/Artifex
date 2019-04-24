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
	user_vote = serializers.SerializerMethodField()		


	class Meta:
		model = Discovery
		fields = ('id',
			'timestamp',
			'title',
			'url',
			'embed',
			'channel_name',
			'author',
			'description',
			'votes',
			'thumbnail',
			 'categories_obj',
			 'comments',
			 'user_vote')
		depth=1

	def get_user_vote(self, obj):
		discovery = Discovery.objects.get(id=obj.id)
		print(self.context.get('request').user.id)
		if self.context.get('request').user.id in discovery.vote:
			discovery.user_vote=True
		else: 
			discovery.user_vote=False
		discovery.save()
		return Discovery.objects.filter(id=discovery.id).values('user_vote')	 	

# class DiscoveryCatalogSerializer(serializers.ModelSerializer):
# 	author = UserSerializer()
# 	class Meta:
# 		model = Discovery
# 		fields = ('id','timestamp','title','author','thumbnail','channel_name','votes')
# 		depth = 1
