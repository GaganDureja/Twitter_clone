from django.urls import path

from . import views


urlpatterns = [
	path('', views.home_view, name='home_view'),
	path('create-tweet', views.tweet_create_view, name='tweet_create_view'),

	path('<int:tweet_id>', views.tweet_detail_view),

]