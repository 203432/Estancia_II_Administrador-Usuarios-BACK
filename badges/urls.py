
from django.urls import re_path

from badges.views.badges_list_views import BadgesList
from badges.views.badges_detail_views import BadgesDetail

urlpatterns = [
    re_path(r'$', BadgesList.as_view()),
    re_path(r'(?P<pk>\d+)$', BadgesDetail.as_view())
]