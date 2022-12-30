import re
from xml.dom.minidom import Document
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from administradorUsuarios import settings

from user.views.profile_list_views import TablaProfileList
from user.views.profile_detail_views import TablaProfileDetail


urlpatterns = [
    re_path(r'$', TablaProfileList.as_view()),
    re_path(r'(?P<pk>\d+)$', TablaProfileDetail.as_view())
]