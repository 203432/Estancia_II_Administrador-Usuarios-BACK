import re
from xml.dom.minidom import Document
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from administradorUsuarios import settings

from user.views import TablaProfileList


urlpatterns = [
    re_path(r'$', TablaProfileList.as_view()),
]