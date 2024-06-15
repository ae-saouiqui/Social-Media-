from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Group_Chat
# Create your views here.

@login_required
def chat(request):
    chats=Group_Chat.objects.filter(members=request.user).order_by('-last_message__timestamp')
    context={
        'user':request.user,
        'chats':chats
    }
    return render(request, 'chat.html', context)
