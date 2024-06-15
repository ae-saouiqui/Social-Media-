from django.contrib.auth.backends import BaseBackend
from .models import MyUser
# Create our custom authentication system

'''
The BaseBackend class require to implements two crucial methods


1. authenticate : 






2. get_user_id: 



'''
class CustomAuthentification(BaseBackend):

    def authenticate(self,request,email,password):
        if MyUser.objects.filter(email=email).exists() and MyUser.objects.filter(password=password).exists():
            return MyUser.objects.get(email=email,password=password)
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except:
            return None

