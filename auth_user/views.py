from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.apple.client import AppleOAuth2Client
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from dj_rest_auth.registration.views import SocialLoginView

import urllib.parse
from django.shortcuts import redirect
from django.urls import reverse

# Google
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "https://izlight.org:8000/api/v1/auth/google/callback/"
    client_class = OAuth2Client
    
    # @property
    # def callback_url(self, request, *args, **kwargs):
    # 	return self.request.build_absolute_uri(reverse('google_callback'))

def google_callback(request, *args, **kwargs):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://izlight.org:8000/google/{params}') #front url

# Facebook
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "https://izlight.org:8000/api/v1/auth/facebook/callback/"
    client_class = OAuth2Client
    
    # @property
    # def callback_url(self, request, *args, **kwargs):
    # 	return self.request.build_absolute_uri(reverse('facebook_callback'))

def facebook_callback(request, *args, **kwargs):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://izlight.org:8000/facebook/{params}') #front url

# Apple PENDIENTE
class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    client_class = AppleOAuth2Client

    @property
    def callback_url(self, request, *args, **kwargs):
    	return self.request.build_absolute_uri(reverse('apple_callback'))

def apple_callback(request, *args, **kwargs):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://izlight.org:8000/apple/{params}') #front url