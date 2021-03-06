import reversion
import uuid
from django.core.validators import validate_email
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.contrib.auth.models import make_password
from django.db import models
from django.utils import timezone
from common.models import TwoFactorEmailDevice, TwoFactorPhoneDevice


class MyUserManager(BaseUserManager):
    """
    Reimplementing the django.contrib.auth.models UserManager
    by extending the BaseUserManager
    """
    def create(self, email, first_name,
               password=None, **extra_fields):
        now = timezone.now()
        validate_email(email)
        p = make_password(password)
        email = MyUserManager.normalize_email(email)
        user = self.model(email=email, first_name=first_name, password=p,
                          is_staff=False, is_active=True, is_superuser=False,
                          date_joined=now, **extra_fields)
        user.save(using=self._db)

        # # add email device
        device = TwoFactorEmailDevice.objects.create(
            user=user, name="Email Device")
        device.generate_challenge()

        # add sms device
        device = TwoFactorPhoneDevice.objects.create(
            user=user, name="SMS Device", number=user.phone_number,
            method="sms")
        device.generate_challenge()
        return user

    def create_superuser(self, email, first_name,
                         password, **extra_fields):
        user = self.create(email, first_name,
                           password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_phone_verified = True
        user.is_email_verified = True
        user.save(using=self._db)
        return user


@reversion.register
class User(AbstractBaseUser):
    """
      Most Acquired from AbstractUser
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=40, unique=True)
    phone_number = models.CharField(
        max_length=120, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        app_label = 'users'
