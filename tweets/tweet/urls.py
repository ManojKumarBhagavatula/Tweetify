from django.urls import path
from .views import *

urlpatterns = [
    
    path('', all_tweets, name='all_tweets'),
    path('create/', make_tweets, name='create_tweets'),
    path('<int:tweet_id>/edit/', edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/', delete_tweet, name='delete_tweet'),
    path('register/', register, name='register'),
    

]