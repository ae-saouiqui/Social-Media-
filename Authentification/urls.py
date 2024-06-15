from django.urls import path
from .views import signup,login
urlpatterns = [
    path('', signup, name='signup'),
    path('accounts/login/',login,name='login')
]
