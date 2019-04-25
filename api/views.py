from django.shortcuts import render, HttpResponse, redirect
from api.models import Discovery, Category, Comments, Subscriber
from api.serializers import DiscoverySerializer, CategorySerializer, CommentSerializer, UserSerializer
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
	queryset = Discovery.objects.all().order_by("-votes")
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
		embed = f"https://www.youtube.com/embed/{string1}"
		thumbnail = f"https://img.youtube.com/vi/{string1}/0.jpg"
		print(thumbnail)
		new_post = Discovery.objects.create(title = title, 
			description =description, 
			channel_name=channel_name,
			url=url, 
			vote=[0],
			categories=categories,
			thumbnail=thumbnail,
			author=request.user,
			embed=embed
			)


		return HttpResponse()


class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer



class CommentView(viewsets.ModelViewSet):
	queryset = Comments.objects.all().order_by("-timestamp")
	serializer_class = CommentSerializer

	def create(self, request):
		comment = request.data['comment']
		user = request.user
		discovery = Discovery.objects.get(id=request.data['discovery'])
		obj = Comments.objects.create(comment=comment,
			user=user,
			discovery=discovery
			)
		return HttpResponse()



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def vote(request, id):

	discovery = Discovery.objects.get(id=id)	
	
	if request.user.id not in discovery.vote:
		discovery.vote.append(request.user.id)
		discovery.votes += 1
		discovery.save()
		print(discovery.votes)
		print(discovery.vote)
		return Response({"message":"Upvoted"})		
	else:
		discovery.vote.remove(request.user.id)
		discovery.votes -= 1
		discovery.save()
		print(discovery.votes)
		print(discovery.vote)
		return Response({"message":"Downvoted"})


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

	
@api_view(['POST'])
@permission_classes((AllowAny,))
def subscribe(request):
	email_id = request.data['email']
	if not Subscriber.objects.filter(email=email_id):
		instance = Subscriber.objects.create(email=email_id)
		return Response({"message":"Subscribed"})
	else:
		return Response({"message":"Already Subscribed"})
			

	