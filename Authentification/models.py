import os

from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin,Group,Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

#Create my custom User Manager
class MyUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Il faut saisir un address email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email=None,password=None,**extra_fields)
    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)


def create_profile_image_directory(instance,filename):
    return f'images/profile_picture/user_{instance.id}/{filename}'
def create_background_image_directory(instance,filename):
    return f'images/background_picture/user_{instance.id}/{filename}'
#create my custom user
class MyUser(AbstractBaseUser,PermissionsMixin):
    firstname: str = models.CharField(max_length=255)
    lastname: str = models.CharField(max_length=255)
    email: str = models.EmailField(unique=True,blank=True)
    phone: str = models.CharField(max_length=10)
    password: str = models.TextField()
    birthday: object = models.DateField()
    profile_picture = models.ImageField(upload_to=create_profile_image_directory,default='images/profile_picture/userdefault.png')
    background_picture = models.ImageField(upload_to=create_background_image_directory,default='images/background_picture/bgdefault.jpg')
    friends=models.ManyToManyField('self',related_name='my_friends')
    is_active :bool= models.BooleanField(default=True)
    is_staff :bool= models.BooleanField(default=False)
    is_superuser :bool= models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True,null=True)

    objects = MyUserManager()


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','birthday','phone','password']

    #Setting meta data for this model
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='myuser_set',  # Change this to a unique related_name
        related_query_name='user',
    )

    # Add or change related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='myuser_set',  # Change this to a unique related_name
        related_query_name='user',
    )




