# Accounts/ Models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, username, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given Username must be set')
        elif not email:
            raise ValueError('The given email must be set')
        #username = self.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self,username, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    # Links UserProfile to a User model instance.
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        #validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)

    mobile = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25, blank=True)
    userbio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    doj = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    job = models.CharField(max_length=50, blank=True)
    skills = models.TextField(max_length=100, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.username
