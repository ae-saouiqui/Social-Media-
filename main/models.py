from django.db import models

# Create your models here.
from django.db import models
from Authentification.models import MyUser
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content=models.TextField(blank=True)
    date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='posts',blank=True,null=True)
    likes=models.IntegerField(default=0)



class FreindsRequest(models.Model):
    sender=models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='receiver')
    date=models.DateTimeField(default=timezone.now)
    accepted=models.BooleanField(default=False)
