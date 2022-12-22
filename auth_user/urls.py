from django.contrib import admin
from django.urls import include, path
from auth_user.views import GoogleLogin, google_callback, FacebookLogin, facebook_callback, AppleLogin, apple_callback
from allauth.socialaccount.providers.google import views as google_views
from allauth.socialaccount.providers.facebook import views as facebook_views
from allauth.socialaccount.providers.apple import views as apple_views

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),

    path('google/connect/', GoogleLogin.as_view(), name='google_connect'),
    path('google/login/', google_views.oauth2_login, name='google_lgoin'),
    path('google/callback/', google_callback, name='google_callback'),

    path('facebook/connect/', FacebookLogin.as_view(), name='facebook_connect'),
    path('facebook/login/', facebook_views.oauth2_login, name='facebook_lgoin'),
    path('facebook/callback/', facebook_callback, name='facebook_callback'),

    path('apple/connect/', AppleLogin.as_view(), name='apple_connect'),
    path('apple/login/', apple_views.oauth2_login, name='apple_lgoin'),
    path('apple/callback/', apple_callback, name='applecallback'),
]