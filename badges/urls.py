
from django.urls import re_path

from badges.views import BadgesList


urlpatterns = [
    re_path(r'$', BadgesList.as_view()),
]