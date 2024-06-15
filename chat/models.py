from django.db import models
from Authentification.models import MyUser
# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Group_Chat(models.Model):
    group_name = models.CharField(max_length=255,blank=True)
    picture_profile=models.ImageField(upload_to='images/Group_Picture/',blank=True)
    members=models.ManyToManyField(MyUser,related_name='members')
    messages=models.ManyToManyField(Message,related_name='messages')
    last_message= models.ForeignKey(Message, on_delete=models.CASCADE, null=True)


    def last_messages(self):
        return self.messages.order_by('-timestamp')




