from django.urls import path,include
from rest_framework import routers 
from api import views

router = routers.DefaultRouter()
router.register('discovery', views.DiscoveryView)
router.register('category', views.CategoryView)






urlpatterns = [

	path('', include(router.urls)),
	path('upvote/<int:id>/', views.upvote),
	path('downvote/<int:id>/', views.downvote),

	
 ]

