from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,FreindsRequest
from Authentification.models import MyUser
from chat.models import Group_Chat
from django.http import JsonResponse
import re
# Create your views here.
"""
@author : Es-saouiqui Amine 
@date : 2024-June-15

"""

"""
Definissons la vue home :
      ---- Deplacer  l'utilisateur vers la page d'acceuill apres avoir s'authentifier .
      ---- Les donnees retourne vers la page apres s'authentifier 
           ====> reqs : correspond au nombre d'invitation envoye
           ====> posts : correspond au posts publie par les membres du reseau 
           ====> friends : correspond aux amis d'utilisateur 
"""
@login_required
def home(request,home_id):
    user=request.user
    friends=MyUser.objects.get(id=user.id).friends.all()
    reqs=FreindsRequest.objects.filter(receiver=user,accepted=False).count()
    request.session.update({'reqs':reqs})
    posts=Post.objects.filter(user__in=list(friends)+[user]).order_by('date').reverse()
    if request.method=='POST':
        data:str=request.body
        data=data.decode('utf-8').removeprefix('{').removesuffix('}').split(':')[1].strip('"')
        data=int(data)
        post=Post.objects.get(id=data)
        post.likes+=1
        post.save()
        return JsonResponse({'likes':post.likes})
    context={'user':user,'reqs':reqs,'friends':friends,'posts':posts}
    return  render(request,'main.html',context)

"""
Definissons la vue post  :
      ---- Publier un post de l'utilsateur
      ---- Enregistrer le post concernant l'utilisateur vers un base de donnee' 
"""
def post(request):
    friends = MyUser.objects.get(id=request.user.id).friends.all()
    context={'reqs':request.session['reqs'],'friends':friends}
    if request.method=='POST':
        post=Post(user=request.user,content=request.POST['text-area'])
        post.save()
        posts = Post.objects.filter(user__in=list(friends)+[request.user]).order_by('date').reverse()
        context.update({'posts':posts})
    return render(request,'main.html',context)



"""
Definissons la vue search_friends qui permet l'utilsateur de chercher aux utilisateurs pour se rencontrer 
"""
def search_friends(request):
    context={'sender':request.user}
    if request.method=='GET':
        search=request.GET['search-friends']
        receivers=FreindsRequest.objects.filter(sender=request.user,accepted=False).values_list('receiver',flat=True)
        user=request.user
        friends=user.friends.values_list('id',flat=True)
        context.update({'receivers':receivers,'friends':friends})
        if n:=len(search.split())>1:
            fname = search.split()[0].strip()
            sname = search.split()[1].strip()
            users = MyUser.objects.filter(firstname=fname.capitalize(), lastname=sname.capitalize())
        else:
            users = MyUser.objects.filter(firstname=search.strip())
            fname = search.strip()
            sname =''
        context.update({'users':users,'fname':fname,'sname':sname})
        return render(request,'result.html',context)
    return render(request,'main.html',context)


"""
La methode send_request qui permet l'utilisateur a envoyee ou bien annnuler  des invitations d'amitie aux autres utilisateurs  """
def send_request(request):
    if request.method=='POST':
        sender=MyUser.objects.get(id=int(request.POST['sender']))
        print(sender.firstname,sender.lastname)
        receiver=MyUser.objects.get(id=int(request.POST['receiver']))
        print(receiver.firstname, receiver.lastname)
        fname=request.POST['fname'].strip()
        sname=request.POST['sname'].strip()
        users=MyUser.objects.filter(firstname=fname,lastname=sname)
        req=request.POST['req']
        context={'sender': request.user, 'users': users, 'sname': sname, 'fname': fname}
        if FreindsRequest.objects.filter(sender=sender,receiver=receiver).exists():
            receivers = FreindsRequest.objects.filter(sender=sender,accepted=False).values_list('receiver',flat=True)
            if FreindsRequest.objects.filter(sender=sender,receiver=receiver,accepted=False).exists():
                if req=='decline':
                    FreindsRequest.objects.get(receiver=receiver,sender=sender).delete()
                    context.update({'receivers':receivers})

        else:
            friend=FreindsRequest(sender=sender,receiver=receiver)
            friend.save()
        return render(request,'result.html',context)
    return render(request,'result.html')

"""

"""
def response_box(request,user_id):
    user=MyUser.objects.get(id=int(user_id))
    friends=FreindsRequest.objects.filter(receiver=user)
    if request.method=='POST':
        match response:=request.POST['add']:
           case 'yes':
            fr=MyUser.objects.get(id=int(request.POST['sender']))
            req=FreindsRequest.objects.get(sender=fr,receiver=user)
            req.accepted=True
            req.save()
            groupe_name="__"
            chat=Group_Chat(group_name=groupe_name)
            chat.save()
            chat.members.add(user)
            chat.members.add(fr)
            chat.save()
            user.friends.add(fr)
            fr.friends.add(user)
            user.save()
            fr.save()
           case 'no':
            fr = MyUser.objects.get(id=int(request.POST['sender']))
            req = FreindsRequest.objects.get(sender=fr, receiver=user)
            req.delete()
    reqs = list(FreindsRequest.objects.filter(receiver=user, accepted=False).values_list('sender',flat=True))
    reqs=MyUser.objects.filter(id__in=reqs)

    return render(request, 'friends_box.html', {'friends': reqs, 'user': user})

def user(request,user_id,visited_id):
    user=MyUser.objects.get(id=int(user_id))
    friends=user.friends.all()
    visited=MyUser.objects.get(id=int(visited_id))
    posts=Post.objects.filter(user=visited).order_by('-date')
    if request.method == 'POST':
        if not 'pictureType' in request.POST:
            body: str = request.body.decode('utf-8').removeprefix('{').removesuffix('}')
            print(body)
            value = body.split(',')[1].split(':')[1].strip('"')
            print(value)
            success = False
            message = ''
            match field := body.split(',')[0].split(':')[1].strip('"'):
                case 'firstname':
                    user.first_name = value.strip()
                    user.save()
                    success = True
                    message = value

                case 'lastname':
                    user.first_name = value.strip()
                    user.save()
                    success = True
                    message = value
                case 'email':
                    if not verify_input('email', value):
                        success = False
                        message = 'Invalid email'
                    elif MyUser.objects.filter(email=value.strip()).exists():
                        success = False
                        message = 'A user with this email already exists'
                    else:
                        user.email = value.strip()
                        user.save()
                        success = True
                        message = value
                case 'phone':
                    if not verify_input('phone', value):
                        print(verify_input('phone', value))
                        success = False
                        message = 'Invalid phone number'
                    elif MyUser.objects.filter(phone=value.strip()).exists():
                        success = False
                        message = 'A user with this phone already exists'
                    else:
                        user.phone = value.strip()
                        user.save()
                        success = True
                        message = value
            return JsonResponse({'success': success, 'message': message})
        else :
            print(request.FILES)
            print(request.POST)
            if 'ProfilePicture' in request.POST['pictureType']:
                profile_picture = request.FILES['imageFile']
                user.profile_picture = profile_picture
                user.save()  # Save the model instance to update the profile picture
                return JsonResponse({'success': True, 'message': 'Profile picture uploaded successfully.','type':'profile','url':user.profile_picture.url})

            elif 'BackgroundPicture' in request.POST['pictureType']:
                background_picture = request.FILES['imageFile']
                user.background_picture = background_picture
                user.save()
                return  JsonResponse({'success': True, 'message': 'Background picture uploaded successfully.','type':'bg','url':user.profile_picture.url})
    return render(request,'profile.html',{'user':user,'friends':friends,'visited':visited_id,'posts':posts})

def verify_input(attribut:str,value:str)->bool:
    match attribut:
        case 'email':
            pattern=re.compile('[^@]+@gmail+\.com')
            return pattern.match(value)
        case 'phone':
            pattern = re.compile('[0-9]+')
            return  pattern.match(value) and len(value)==10
        case _:
            return False

def create_post(request,user_id):
    user=MyUser.objects.get(id=user_id)
    friends = MyUser.objects.get(id=user.id).friends.all()
    reqs=FreindsRequest.objects.filter(receiver=user,accepted=False).count()
    request.session.update({'reqs':reqs})
    if request.method=='POST':
        post=Post(user=user,content=request.POST['post-desc'],image=request.FILES['post_image'])
        post.save()
        posts=Post.objects.filter(user__in=list(friends)+[user]).order_by('date').reverse()
        context = {'user': user, 'reqs': reqs, 'friends': friends, 'posts': posts}
        return render(request,'main.html',context)
    return render(request,'post.html',{'user':user})







