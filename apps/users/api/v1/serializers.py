from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_jwt.compat import Serializer, PasswordField
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

User = get_user_model()


class CustomJSONWebTokenSerializer(Serializer):

    email = serializers.EmailField(max_length=25,)

    password = PasswordField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        credentials = {
            'email': email,
            'password': password
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                if user.is_blocked:
                    msg = 'Something went wrong, Please Contact further detail'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg)

        msg = 'Must include "Email" and "password".'
        raise serializers.ValidationError(msg)
