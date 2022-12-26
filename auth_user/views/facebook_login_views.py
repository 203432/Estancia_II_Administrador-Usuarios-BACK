from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from dj_rest_auth.registration.views import SocialLoginView

import urllib.parse
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes

# Facebook
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "https://izlight.org:8000/api/v1/auth/facebook/callback/"
    client_class = OAuth2Client
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def facebook_callback(request, *args, **kwargs):
    code = request.GET
    # params = urllib.parse.urlencode(request.GET)
    return Response(code['code'], status=status.HTTP_200_OK)
    # return redirect(f'https://izlight.org:8000/facebook/{params}') #front url
