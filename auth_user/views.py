from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.apple.client import AppleOAuth2Client
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from dj_rest_auth.registration.views import SocialLoginView

import urllib.parse
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes

# Google
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "https://izlight.org:8000/api/v1/auth/google/callback/"
    client_class = OAuth2Client
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def google_callback(request, *args, **kwargs):
    code = request.GET
    # params = urllib.parse.urlencode(request.GET)
    return Response(code['code'], status=status.HTTP_200_OK)
    # return redirect(f'https://izlight.org:8000/google/{params}') #front url

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

# Apple PENDIENTE
class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    client_class = AppleOAuth2Client

    @property
    def callback_url(self, request, *args, **kwargs):
    	return self.request.build_absolute_uri(reverse('apple_callback'))

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apple_callback(request, *args, **kwargs):
    code = request.GET
    # params = urllib.parse.urlencode(request.GET)
    return Response(code['code'], status=status.HTTP_200_OK)
    # return redirect(f'https://izlight.org:8000/apple/{params}') #front url