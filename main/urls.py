from django.urls import path
from .views import home,post,search_friends,send_request,response_box,user,create_post
urlpatterns = [
path('home/<int:home_id>/',home,name='home'),
path('home/post',post,name='post'),
path('home/search_firends/',search_friends,name='searchfriends'),
path('home/search_firends/send',send_request,name='request'),
path('home/response_box/<int:user_id>/',response_box,name='friends_box'),
path('home/user_profile/<int:user_id>/<int:visited_id>/',user,name='user_profile'),
path('home/create_post/<int:user_id>/',create_post,name='create_post')
]