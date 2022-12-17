from django.urls import path, re_path
from django.conf.urls import include

from AdministradorRutas.views import routesList
from AdministradorRutas.views import routesDetail

urlpatterns = [
    re_path(r'$', routesList.as_view()),
    re_path(r'(?P<pk>\d+)$', routesDetail.as_view())
    
]