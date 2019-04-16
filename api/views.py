from django.shortcuts import render, HttpResponse, redirect
from api.models import Discovery, Category, Comments
from api.serializers import DiscoverySerializer, CategorySerializer, DiscoveryCatalogSerializer, CommentSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action 
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.db.models import F
from rest_framework import status

class DiscoveryView(viewsets.ModelViewSet):
	queryset = Discovery.objects.all()
	serializer_class = DiscoverySerializer
	
	
	def create(self, request):
		title = request.data['title']
		description = request.data['description']
		channel_name = request.data['channel_name']
		url = request.data['url']
		categories = request.data['categories']
		thumb = str(url).split("=")
		print(url)
		string1 = str(thumb[1])
		thumbnail = f"https://img.youtube.com/vi/{string1}/0.jpg"
		print(thumbnail)
		new_post = Discovery.objects.create(title = title, 
			description =description, 
			channel_name=channel_name,
			url=url, 
			categories=categories,
			thumbnail=thumbnail,
			)


		return HttpResponse()




	def list(self, request):
		 queryset = Discovery.objects.all()
		 serializer = DiscoveryCatalogSerializer(queryset, many=True)
		 return Response(serializer.data)
	





class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer



class CommentView(viewsets.ModelViewSet):
	queryset = Comments.objects.all()
	serializer_class = CommentSerializer



def upvote(request, id):
	discovery = Discovery.objects.filter(id=id).update(votes=F('votes') + 1)
	return HttpResponse()



def downvote(request, id):
	discovery = Discovery.objects.filter(id=id).update(votes=F('votes') - 1)	
	return HttpResponseRedirect( )		



