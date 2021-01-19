import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from apps.commons.helpers import get_upload_path
from apps.commons.models import BaseModel
from apps.users.constants import GENDER_CHOICES
from apps.users.manager import UserManager

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,20}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class User(AbstractUser, BaseModel):
    """
    User model

    :cvar email: Primary email of user.
        Can be used to log in.
        There should be one UserEmail associated with this email address
        with primary set to True.

    """
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={'unique': "A user with that username already exists."},
        default=uuid.uuid4
    )

    first_name = models.CharField(max_length=150)

    middle_name = models.CharField(max_length=150, blank=True, null=True)

    last_name = models.CharField(max_length=150)

    profile_picture = models.ImageField(
        upload_to=get_upload_path,
        blank=True
    )

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        }
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True, null=True
    )

    is_blocked = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    @property
    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"
