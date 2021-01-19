import six
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import Http404
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

User = get_user_model()


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active) +
            six.text_type(login_timestamp)
        )


token_generator = TokenGenerator()
