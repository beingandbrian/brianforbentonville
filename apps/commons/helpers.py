import os
import uuid
import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def get_today():
    return timezone.now().astimezone().date()


def get_uuid_filename(filename):
    """
    rename the file name to uuid4 and return the
    path
    """
    ext = filename.split('.')[-1]
    return "{}.{}".format(uuid.uuid4().hex, ext)


def get_upload_path(instance, filename):
    return os.path.join(f"uploads/{instance.__class__.__name__.lower()}",
                        get_uuid_filename(filename))


def popover_html(label, content):
    return label + '<button tabindex = "0" class = "simple-btn" \
    type = "button" title="' + label + '" data-toggle = "popover" \
        data-toggle = "hover" data-trigger = "click" \
        data-html = "true" data-content = "' + content + '" > \
        <span class = "fa fa-question-circle-o"></span></button>'


def get_user_from_email(email):
    """get user for given email"""
    try:
        user = User.objects.get(email=email)
    except Exception as e:
        return None
    return user


def get_user_from_uidb64(uidb64):
    """get user from base64 encoded userid"""
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception as e:
        return None
    return user
