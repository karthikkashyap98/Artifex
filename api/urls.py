from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers 
from api import views




router = routers.DefaultRouter()
router.register('discovery', views.DiscoveryView)
router.register('category', views.CategoryView)
router.register('comments',views.CommentView)
router.register('filter', views.FilterView, base_name="FilterView")
router.register('signup', views.Signup, base_name='Signup')


urlpatterns = [

	path('', include(router.urls)),
	path('upvote/<int:id>/', views.upvote),
	path('downvote/<int:id>/', views.downvote),
 ]

