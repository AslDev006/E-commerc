from django.db import models
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
# from django_resized import ResizedImageField

ordinary = 'ordinary'
manager = 'manager'
admin = 'admin'
superadmin = 'superadmin'
courier = 'courier'
via_email = 'via_email'
via_phone = 'via_phone'
active = 'active'
deactive = 'deactive'


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    USER_TYPES = (
        (ordinary, ordinary),
        (manager, manager),
        (admin, admin),
        (superadmin, superadmin),
        (courier, courier)
    )

    AUTH_TYPE = (
        (via_email, via_email),
        (via_phone, via_phone)
    )

    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    user_type = models.CharField(max_length=25, choices=USER_TYPES, default=ordinary),
    auth_type = models.CharField(max_length=25, choices=AUTH_TYPE)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField()
    # avatar = ResizedImageField(verbose_name='image',
    #                            size=[400, 400],
    #                            crop=['middle', 'center'],
    #                            null=True, blank=True,
    #                            upload_to='user_avatars/')
    avatar = models.ImageField(upload_to='user_avatars/')