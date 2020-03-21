from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# read-more, creating a custom user model manager
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name=None):
        if not email:
            raise ValueError("Please Enter a valid email")
        if not password:
            raise ValueError("Please enter a valid password")
        user= self.model(
            email=self.normalize_email(email), 
            name=name
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password, name):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

# read-more
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model
# creating a custom user model
class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email' #used as the username, i.e., login 
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin