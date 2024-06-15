from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import *
import json

from asgiref.sync import sync_to_async,async_to_sync
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id=int(self.scope['path'].split('/')[3])
        self.group_chat=Group_Chat.objects.get(id=self.room_id)
        async_to_sync(self.channel_layer.group_add)(
            self.group_chat.group_name, self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.group_chat.group_name, self.channel_name
        )
    def receive(self,text_data):
        text=json.loads(text_data)
        command=text['command']
        if command=='fetch_messages':
            messages=self.group_chat.last_messages()
            context=[{'message':message.content,'author':message.author.id,'time': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),'url':message.author.profile_picture.url} for message in messages]
            print(context)
            async_to_sync(self.channel_layer.group_send)(
                self.group_chat.group_name,{
                    'type':'fetch_messages',
                    'messages':None if not context else context,

                }
            )
        elif command=='chat_message':
            sender = MyUser.objects.get(id=text['sender'])
            message = Message(content=text['message'], author=sender)
            print(message.content)
            message.save()
            self.group_chat.messages.add(message)
            self.group_chat.last_message=message
            self.group_chat.save()
            print(self.group_chat.last_message)
            async_to_sync(self.channel_layer.group_send)(
                self.group_chat.group_name,
                {
                    'type': 'chat_message',
                    'sender': sender.id,
                    'message': message.content,
                    'url':sender.profile_picture.url
                }
            )
    def fetch_messages(self,event):
        messages=event['messages']
        self.send(text_data=json.dumps({'type':'fetch_messages','messages':messages}))

    def chat_message(self,event):
        message=event['message']
        sender=event['sender']
        print("Received message from group:", message)
        self.send(text_data=json.dumps({'type':'chat_message','message':message,
                                        'sender':sender}))