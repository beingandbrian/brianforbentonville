from django.urls import path

from apps.users.api.v1.views import CustomObtainJSONWebToken
app_name = 'users'

urlpatterns = [
    path('get-token/', CustomObtainJSONWebToken.as_view(), name='get_token'),
]
