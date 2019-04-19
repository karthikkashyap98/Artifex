from django.shortcuts import render, HttpResponse, redirect
from api.models import Discovery, Category, Comments
from api.serializers import DiscoverySerializer, CategorySerializer, DiscoveryCatalogSerializer, CommentSerializer, UserSerializer
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action 
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.db.models import F
from rest_framework import status
import django_filters
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework.decorators import action, permission_classes, api_view


class DiscoveryView(viewsets.ModelViewSet):
	queryset = Discovery.objects.all()
	serializer_class = DiscoverySerializer
	permission_classes = [IsAuthenticatedOrReadOnly , ]

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
			author=request.user
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
	return HttpResponse()		



class FilterView(viewsets.ModelViewSet):
	serializer_class = DiscoverySerializer

	def get_queryset(self):
		categories = self.request.data["categories_list"]
		queryset = Discovery.objects.filter(categories__contains=categories)
		return queryset


class Signup(viewsets.ViewSet):
	permission_classes = [AllowAny,]

	def create(self, request):
		username = request.data['username']
		userexists = User.objects.filter(username=username)
		if not userexists:
			password = request.data['password']
			email = request.data['email_id']
			first_name = request.data['first_name']
			last_name = request.data['last_name']
			user = User.objects.create_user(username=username,
				password=password,
				email=email,
				first_name=first_name,
				last_name=last_name
				)
			return HttpResponse('done')
		else:
			return HttpResponse(status=404)	

	


