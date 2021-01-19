from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import CustomJSONWebTokenSerializer


class CustomObtainJSONWebToken(ObtainJSONWebToken):
    serializer_class = CustomJSONWebTokenSerializer
